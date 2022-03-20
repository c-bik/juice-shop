/*
 * Copyright (c) 2014-2022 Bjoern Kimminich & the OWASP Juice Shop contributors.
 * SPDX-License-Identifier: MIT
 */

require('./lib/startup/validateDependencies')().then(() => {
  const cluster = require('cluster')
  const app = require('./server')

  const workers: any = {}
  const count = require('os').cpus().length

  function spawn () {
    const worker = cluster.fork()
    workers[worker.pid] = worker
    return worker
  }

  if (cluster.isMaster) {
    for (let i = 0; i < count; i++) {
      spawn()
    }
    cluster.on('death', function (worker: any) {
      console.log('worker ' + worker.pid + ' died. spawning a new process...')
      delete workers[worker.pid]
      spawn()
    })
  } else {
    app.listen(process.env.PORT ?? 5000)
  }
})