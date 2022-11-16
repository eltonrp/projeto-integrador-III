const express = require('express')
const cors = require('cors')
const app = express()


// Procedimentos da documentação Cors para o back-end aceitar as requisições
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*')
  res.header('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE')
  res.header('Access-Control-Allow-Headers', 'X-PINGOTHER, Content-Type, Authorization')
  app.use(cors())
  next()
})

const Home = require('./models/Home')

app.use(express.json())

app.get('/getupdate/:id', async(req, res) => {
  const { id }= req.params
  await Home.findByPk(id, {attributes: ['id', 'name', 'address', 'cep', 'phone']})
  .then((datahome) => {
    return res.json({
      datahome
    })
  })
})

app.get('/', async (req, res) => {
  // Busca todos os registros para mostrar
  await Home.findAll({
    attributes: ['id', 'name', 'address', 'cep', 'phone']
  })
    .then((datahome) => {
      return res.json({
        erro: false,
        datahome
      })
    }).catch(() => {
      return res.status(400).json({
        erro: true,
        mensagem: 'Erro: nenhum valor encontrado'
      })
    })
})

app.post('/post', async (req,res) => {
  await Home.create(req.body)
  .then(() => {
    return res.json({
      erro: false,
      mensagem: 'Cadastro realizado com sucesso'
  })
  }).catch(() => {
    return res.json({
      erro: true,
      mensagem: 'Erro: Dados não cadastrados'
    })
  })
})

app.delete('/delete/:id', async(req, res) => {
  const  { id }  = req.params
  console.log(id)
  await Home.destroy({
    where: {
      id: id
    }
  }).then(() => {
    return res.status(200).json({
      erro: false,
      mensagem: 'Ponto de Coleta apagado com sucesso'
    })
  }).catch(() => {
    return res.status(401).json({
      erro: true,
      mensagem: 'Erro: Ponto de coleta não encontrado'
    })
  })
})

app.put('/update/:id', async(req, res) => {
  const { id } = req.params
  const dataUpdate  = req.body
  await Home.update(dataUpdate, {
    where: {
      id: id
    }
  }).then(() => {
    return res.json({
      erro: false,
      mensagem: 'Registro Atualizado'
    })
  }).catch(() => {
    return res.status(401).json({
      erro: true,
      mensagem: 'Algo deu errado, tente novamente'
    })
  })
})

//Heroku utiliza portas própias
//Portanto deve-se usar as variáveis abaixo
app.listen(process.env.PORT || PORT, () => {
  console.log(`Server iniciado...`)
})