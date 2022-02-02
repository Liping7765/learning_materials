"""

1. AWS Global Infrastructure 

Avaibility Zone is composed of one or more data centers

Region has at least 2 Availability Zones, totaling 24 region around the world 

Each region is totally independent of each other 


2. AWS Pricing 
    a. computing - the ram and duration 
    b. storage - quantity of data stored
    c. outbound - quantity of data that is transferred out 

3. IAM Overview 

  IAM Policy : pre-set access rights   
  IAM User --> IAM Group --> IAM Role 


  Authentification:
  Access Key  -> API 
  IAM User --> Password  --> AWS Managment Console 

  How to create IAM user

  AWS management console -> security, identity, compliance -> IAM -> (update a better signin link) --
  -> create a group and assign policy -> create a IAM user -> add the user to a group 

4. Amazon Virtual Private Cloud (VPC)
            contain
    Region -----------> VPC -> avalibility zone -> subnet (public and private) -> instance 

    VPC is represented by CIDR Block 


5. Security Group and Network Access Control Lists,

    Security Group applys at the instance level -> stateful firewall 

    Network ACL applys at the subnet level to control the trafic -> stateless firewall 

    Stateful firewalls vs stateless firewalls 

    statefull firewalls allow outbound return automatically if inbound is allowed 
    stateless firewalls will check both inbound and outbound 

"""