# Infrastructure as Code
## **What is it? Why would I want it? Are there any alternatives ?**
*Infrastructure as code is a way of describing all the components needed to run some application, allowing you to automate all the configuration and replicate as many times as required across several different cloud providers.*

*Using an IaC tool like terraform, in conjunction with some version control like git, allows you to have insight into how infrastructure components have changed over time. If you can prevent any manual changes to the infrastructure (immutable), it allows you greater control and ease in managing it.*

*In my opinion, using an IaC tool together with a CI/CD pipeline and a configuration management tool like Ansible, Chef, or Puppet is fundamental for any development team.*

# Observability
## **Please explain this term in the context of micro services. What do we want to observe? What kind of challenges do you see in a distributed environment? How can we solve them?**
*For a microservices context, it is essential to observe the health of the services and all their communications dependencies, whether internal or external. In distributed environments, many components and their interdependencies can make it very difficult to monitor and troubleshoot problems.* 

*Classic monitoring tools like Zabbix / Nagios together with APMs like Datadog or NewRelic are a reasonable basis, and using modern tools like istio (service mesh), ELK, Prometheus, Grafana, Splunk, and the specialized products of cloud providers like Cloudwatch can help to have good observability of the environment.*


# Security
## **Imagine you would join our team and put in charge of securing our AWS infrastructure. What are the first three things that you check, to limit the risk of a breach? Explain why.**

*1 - Use a tool to discover possible secrets in the repositories because this is one of the leading causes of security breaches, which can cause considerable financial damage to the company.*

*2 - Review the access control to Cloud providers, and adopt a model where no one can create or change anything manually, only through some automated and validated process. This way, it is possible to have greater control and enables the tracking of everything that is created and changed in the environment.*

*3 - Use a static analysis tool like SonarQube in the CI/CD pipeline in a way that no deployment can be done in the environment if it does not pass the parameters defined by the company/team/squad, trying to ensure a minimum of acceptable quality for the code that goes to production.*

