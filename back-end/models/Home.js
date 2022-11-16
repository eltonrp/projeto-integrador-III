const Sequelize = require('sequelize')
const db = require('./db')

const Home = db.define('pontos', {
  id: {
    type: Sequelize.INTEGER,
    autoIncrement: true,
    allowNull: false,
    primaryKey: true
  },
  name: {
    type: Sequelize.STRING,
    allowNull: false,
  },
  address: {
    type: Sequelize.STRING,
    allowNull: false
  },
  cep: {
    type: Sequelize.INTEGER
  },
  phone: {
    type: Sequelize.BIGINT
  }
})

// Cria a tabela IF NOT EXITS
// Home.sync()
// Cria a tabela no db e verifica alterações
// Home.sync({ alter: true })
// Cria a tabela, apagando primeira se alguma existir
// Home.sync({ force: true }) 

module.exports = Home