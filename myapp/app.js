const express = require('express')
const app = express()
const port = 3000


app.get('/', function (req, res) {
    res.send('Hello Wdddddddorld!')
})

app.post('/', function (req, res) {
    res.send('Got a POST request')
  })
app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))



