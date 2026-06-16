// npm init
// npm i express
// RAPIDAPI CLIENT
// http localhost : 3000 / clientes/...

const express = require('express')
const app = express()
const port = 3000
app.use(express.json())
const fs = require('fs')

app.get('/ola', (req, res)=>{
    res.json('hello class')
})

app.post("/musicas", (req,res) => {
    const musica = req.body
    if (!musica || Object.keys(musica).length === 0) {
        res.status(400).json({resposta: "Body não preenchido"})
    } else {
        try {
            const bd = JSON.parse(fs.readFileSync('bd.json', 'utf8'))
            bd.push(musica)
            fs.writeFileSync('bd.json', JSON.stringify(bd), 'utf8')
            res.status(201).json({resposta: "Cliente cadastrado com sucesso!"})
        } catch(error) {
            res.status(500).json({resposta: error.message})
        }
    }    
})
app.get("/musicas", (req, res) => {
    try{
        const musicas = JSON.parse(fs.readFileSync("bd.json", "utf8"))
        res.status(200).json(musicas)
    }catch(error) {
        res.status(500).json({resposta: error.message})
    }

})

app.get("/musicas/:id", (req, res) => {
    const id = req.params.id
    try{
        const musicas = JSON.parse(fs.readFileSync("bd.json", "utf8"))
       const musica_encontrada = musicas.find((musica) => musica.id.replace(/\D/g, "") == id)
       if(!musica_encontrada) {
        res.status(404).json({erro: "cliente não existe no banco de dados! "})
       }
       res.status(200).json(musica_encontrada)
    }catch(error) {
        res.status(500).json({resposta: error.message})
    }

})


app.delete("/musicas/:id", (req, res) => {
    const id = req.params.id
    try{
        const musicas = JSON.parse(fs.readFileSync("bd.json", "utf8"))
       const indice = musicas.findIndex((musica) => musica.id.replace(/\D/g, "") == id)
       if(indice == -1){
        res.status(404).json({resposta: "musica não existe no banco de dados"})
       }
        musicas.splice(indice, 1)
        fs.writeFileSync('bd.json', JSON.stringify(musicas), 'utf8')
       res.status(200).json({resposta: "musica removido"})
    }catch(error) {
        res.status(500).json({resposta: error.message})
    }
    musica.findindex("musicas/:id3") 
    
})

app.put("/clientes/:cpf", (req, res) => {
    const id = req.params.id
    const dados = req.body
    try{
        const musicas = JSON.parse(fs.readFileSync("bd.json", "utf8"))
       const indice_musica = musicas.findIndex((musica) => musica.id.replace(/\D/g, "") == id)
       if(indice_musica == -1){
        return res.status(404).json({resposta: "essa musica não existe no banco de dados"})
       }
        musicas [ indice_musica] = dados
        fs.writeFileSync('bd.json', JSON.stringify(musicas), 'utf8')
       res.status(200).json({resposta: "musica alterada com sucesso"})
    }catch(error) {
        res.status(500).json({resposta: error.message})
    }
    
})



app.listen(port, ()=> {
    console.log('API executado com sucesso' + port)
})
