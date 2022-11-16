const { Sequelize } = require('sequelize')

// Conexão Heroku
const sequelize = new Sequelize('heroku_********', '**************', '**************', {
  host: '**************',
  dialect: 'mysql'
})

// Imprime msg de sucesso ou erro. Usa-se apenas para desenvolvimento
// sequelize.authenticate()
// .then(() => {
//   console.log('Conexão com banco de dados realizada com sucesso')
// }).catch(() => {
//   console.log('Erro: Não foi possível realizar a conexão com o banco de dados')
// })

module.exports = sequelize