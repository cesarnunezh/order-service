@Library('devops-shared-lib@main') _

ciPipeline(
  serviceName: 'orders-api',
  enableDeploy: true,
  dockerRepo: 'cesarnunezh/orders-api',
  localImageName: 'orders-api:ci-local',
  imageBuildCmd: 'make build',
  buildCmd: 'make setup',
  lintCmd: 'make lint',
  testCmd: 'make test',
  securityCmd: 'make scan',
  deployRepo: 'https://github.com/cesarnunezh/DevOpsProject.git'
)
