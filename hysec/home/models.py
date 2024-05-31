from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils.timezone import now




courses = [("Devop","Devop")]
genders=[("Male","Male"),("Female","Female")]

class Profile(models.Model):
  id=models.AutoField(primary_key=True)
  user = models.OneToOneField(User,on_delete=models.CASCADE, null=True) 
  education = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  gender=models.CharField(max_length=50,choices=genders)
  course = models.CharField(max_length=50,choices=courses)
  photo = models.ImageField(upload_to="studentimages",blank=True, null=True)
  date = models.DateField(default= now)
  

  def __str__(self):
    return str(self.user)






htitle=(("Module-1: AWS Cloud Feature and Services","Module-1: AWS Cloud Feature and Services"),
          ("Module-2: Amazon Linux | Centos","Module-2: Amazon Linux | Centos"),
          ("Module-3: DevOps methodology","Module-3: DevOps methodology"),
          ("Module-4: Git and GitHub Version Control System","Module-4: Git and GitHub Version Control System"),
          ("Module-5: Jenkins CI/CD Pipeline","Module-5: Jenkins CI/CD Pipeline"),
          ("Module-6: Docker containerization","Module-6: Docker containerization"),
          ("Module-7: Orchestration (Kubernetes)","Module-7: Orchestration (Kubernetes)"),
          ("Module-8: Ansible Automation Configuration Tool","Module-8: Ansible Automation Configuration Tool"),
          ("Module-9: Terraform IAC Tool","Module-9: Terraform IAC Tool"),
          ("Module-10: Grafana Observability and Monitoring","Module-10: Grafana Observability and Monitoring"))


title=(("MODULE-1: AWS Free Tier Account Activation and Enabling AWS Services and Features","MODULE-1: AWS Free Tier Account Activation and Enabling AWS Services and Features"),
         ("MODULE-1: Creating a Windows Server 2022 EC2 Instance and Establishing Connectivity Using RDP","MODULE-1: Creating a Windows Server 2022 EC2 Instance and Establishing Connectivity Using RDP"),
         ("MODULE-1: Understanding Storage Types and Creating an S3 Bucket with Enabled Features","MODULE-1: Understanding Storage Types and Creating an S3 Bucket with Enabled Features"),
         ("MODULE-1: Creating a Security Group, Adding TCP Rules, and Installing/Publishing an IIS Web Server","MODULE-1: Creating a Security Group, Adding TCP Rules, and Installing/Publishing an IIS Web Server"),
         ("MODULE-1: Creating a Default VPC, Customizing VPC Settings, and Establishing Peering Between Local and Global VPCs","MODULE-1: Creating a Default VPC, Customizing VPC Settings, and Establishing Peering Between Local and Global VPCs"),
         ("MODULE-1: AWS Identity and Access Management (IAM), User and Group Role-Based Permissions, and Policies","MODULE-1: AWS Identity and Access Management (IAM), User and Group Role-Based Permissions, and Policies"),
         ("MODULE-1: AWS Auto-Scaling and Load Balancing, Application and Network Load Balancing","MODULE-1: AWS Auto-Scaling and Load Balancing, Application and Network Load Balancing"),
         ("MODULE-1: AWS Virtual Private Network (VPN) for Secure Communication Over the Internet","MODULE-1: AWS Virtual Private Network (VPN) for Secure Communication Over the Internet"),
         ("MODULE-1: Configuring and Hosting a Static Website on AWS Cloud with Route 53","MODULE-1: Configuring and Hosting a Static Website on AWS Cloud with Route 53"),
         ("MODULE-1: Understanding Databases and Establishing Connectivity Between Cloud and On-Premises Environments","MODULE-1: Understanding Databases and Establishing Connectivity Between Cloud and On-Premises Environments"),
         ("MODULE-2: Amazon Linux EC2 Instance and Establishing Connectivity Using PuttyGen and Putty","MODULE-2: Amazon Linux EC2 Instance and Establishing Connectivity Using PuttyGen and Putty"),
         ("MODULE-2: Learning and Using Linux File and Directory Operation Commands","MODULE-2: Learning and Using Linux File and Directory Operation Commands"),
         ("MODULE-2: Learning and Using Linux User and Group Management and System Control Commands","MODULE-2: Learning and Using Linux User and Group Management and System Control Commands"),
         ("MODULE-2: Learning and Using Linux Networking and System Information Commands","MODULE-2: Learning and Using Linux Networking and System Information Commands"),
         ("MODULE-2: Learning and Using Linux Archiving, Compression, Permissions, and Security Commands","MODULE-2: Learning and Using Linux Archiving, Compression, Permissions, and Security Commands"),
         ("MODULE-2: Amazon Linux EC2 Instance Installation of Web Server (httpd) and Publishing a Webpage","MODULE-2: Amazon Linux EC2 Instance Installation of Web Server (httpd) and Publishing a Webpage"),
         ("MODULE-2: Amazon Linux EC2 Instance Installation of Web Server (Nginx) and Publishing a Webpage","MODULE-2: Amazon Linux EC2 Instance Installation of Web Server (Nginx) and Publishing a Webpage"),
         ("MODULE-2: Linux Security with Ssh-Keygen and IP Tables Commands","MODULE-2: Linux Security with Ssh-Keygen and IP Tables Commands"),
         ("MODULE-2: Basic Bash Scripting","MODULE-2: Basic Bash Scripting"),
         ("MODULE-2: Bash Scripting with Examples","MODULE-2: Bash Scripting with Examples"),
         ("MODULE-3: Evolution of DevOps from Agile","MODULE-3: Evolution of DevOps from Agile"),
         ("MODULE-3: DevOps Engineer Skills in the Market","MODULE-3: DevOps Engineer Skills in the Market"),
         ("MODULE-3: Understanding the DevOps Delivery Pipeline","MODULE-3: Understanding the DevOps Delivery Pipeline"),
         ("MODULE-3: Market Trends in DevOps","MODULE-3: Market Trends in DevOps"),
         ("MODULE-3: DevOps Technical Challenges and Tools","MODULE-3: DevOps Technical Challenges and Tools"),
         ("MODULE-3: DevOps Tools and Platforms","MODULE-3: DevOps Tools and Platforms"),
         ("MODULE-4: Git Installation and Configuration on EC2 Instance and Local Machine","MODULE-4: Git Installation and Configuration on EC2 Instance and Local Machine"),
         ("MODULE-4: GitHub Account Activation, Secret Key Generation, and Creating Public/Private Repositories","MODULE-4: GitHub Account Activation, Secret Key Generation, and Creating Public/Private Repositories"),
         ("MODULE-4: GitHub Integration with Local Repository","MODULE-4: GitHub Integration with Local Repository"),
         ("MODULE-4: Git Operations and Code Push to GitHub or Gitlab","MODULE-4: Git Operations and Code Push to GitHub or Gitlab"),
         ("MODULE-4: Advanced Git Operations with Source Code","MODULE-4: Advanced Git Operations with Source Code"),
         ("MODULE-4: Creating an Environment for Developers with 1 Local Repository and 1 Remote Repository","MODULE-4: Creating an Environment for Developers with 1 Local Repository and 1 Remote Repository"),
         ("MODULE-4: Creating an Environment for Developers with 2 Local Branches/Repositories and 1 Remote Repository","MODULE-4: Creating an Environment for Developers with 2 Local Branches/Repositories and 1 Remote Repository"),
         ("MODULE-4: Creating an Environment for Developers with 4 Local Branches/Repositories and 1 Remote Repository","MODULE-4: Creating an Environment for Developers with 4 Local Branches/Repositories and 1 Remote Repository"),
         ("MODULE-4: Pulling/Committing Code from GitHub","MODULE-4: Pulling/Committing Code from GitHub"),
         ("MODULE-4: Project","MODULE-4: Project"),
         ("MODULE-5: Jenkins Installation and Account Configuration","MODULE-5: Jenkins Installation and Account Configuration"),
         ("MODULE-5: Jenkins Plugin and User Management","MODULE-5: Jenkins Plugin and User Management"),
         ("MODULE-5: Jenkins Features and Services","MODULE-5: Jenkins Features and Services"),
         ("MODULE-5: Jenkins Integration with GitHub to Pull Source Code","MODULE-5: Jenkins Integration with GitHub to Pull Source Code"),
         ("MODULE-5: Jenkins Job Creation and Building Jobs with Shell Execution","MODULE-5: Jenkins Job Creation and Building Jobs with Shell Execution"),
         ("MODULE-5: Creating a CI/CD Pipeline Using Jenkins","MODULE-5: Creating a CI/CD Pipeline Using Jenkins"),
         ("MODULE-5: Creating a CI/CD Pipeline for Automated Deployment","MODULE-5: Creating a CI/CD Pipeline for Automated Deployment"),
         ("MODULE-5: Creating a CI/CD Pipeline for Testing Environments","MODULE-5: Creating a CI/CD Pipeline for Testing Environments"),
         ("MODULE-5: Creating a CI/CD Pipeline for Automated Deployment on AWS","MODULE-5: Creating a CI/CD Pipeline for Automated Deployment on AWS"),
         ("MODULE-5: Automating Deployment Processes with Jenkins","MODULE-5: Automating Deployment Processes with Jenkins"),
         ("MODULE-6: Docker Installation on Amazon Linux EC2","MODULE-6: Docker Installation on Amazon Linux EC2"),
         ("MODULE-6: Docker Basic Operational Commands","MODULE-6: Docker Basic Operational Commands"),
         ("MODULE-6: Docker Hub Account Activation and Image Pull/Search","MODULE-6: Docker Hub Account Activation and Image Pull/Search"),
         ("MODULE-6: Docker Image Pull and Commit","MODULE-6: Docker Image Pull and Commit "),
         ("MODULE-6: Creating a Dockerfile","MODULE-6: Creating a Dockerfile"),
         ("MODULE-6: Docker Run, Build, and Deploy Containers","MODULE-6: Docker Run, Build, and Deploy Containers"),
         ("MODULE-6: Adding Volumes to Containers","MODULE-6: Adding Volumes to Containers"),
         ("MODULE-6: Docker Port Mapping and Networking","MODULE-6: Docker Port Mapping and Networking"),
         ("MODULE-6: Docker Security","MODULE-6: Docker Security"),
         ("MODULE-6: Running Web Applications with Docker Containers (e.g., Nagios or Jenkins)","MODULE-6: Running Web Applications with Docker Containers (e.g., Nagios or Jenkins)"),
         ("MODULE-7: Kubernetes Cluster Installation and Configuration of Minikube","MODULE-7: Kubernetes Cluster Installation and Configuration of Minikube"),
         ("MODULE-7: Creating Pods in a Kubernetes Cluster","MODULE-7: Creating Pods in a Kubernetes Cluster"),
         ("MODULE-7: Creating Multi-Container Pods","MODULE-7: Creating Multi-Container Pods"),
         ("MODULE-7: Creating Namespaces in a Kubernetes Cluster","MODULE-7: Creating Namespaces in a Kubernetes Cluster"),
         ("MODULE-7: Creating Pods in a Specific Namespace","MODULE-7: Creating Pods in a Specific Namespace"),
         ("MODULE-7: Creating Multi-Container Pods with Environment Variables","MODULE-7: Creating Multi-Container Pods with Environment Variables"),
         ("MODULE-7: Creating Deployments and Replica Sets","MODULE-7: Creating Deployments and Replica Sets"),
         ("MODULE-7: Opening Port 80 in a Pod","MODULE-7: Opening Port 80 in a Pod"),
         ("MODULE-7: Creating Replication Controllers","MODULE-7: Creating Replication Controllers"),
         ("MODULE-8: Ansible Installation and Configuration","MODULE-8: Ansible Installation and Configuration"),
         ("MODULE-8: Ansible Setup for Master and Nodes","MODULE-8: Ansible Setup for Master and Nodes"),
         ("MODULE-8: Creating YAML Scripts for Playbooks","MODULE-8: Creating YAML Scripts for Playbooks"),
         ("MODULE-8: Creating Ansible Playbooks","MODULE-8: Creating Ansible Playbooks"),
         ("MODULE-8: Implementing Playbooks and Ansible Automation","MODULE-8: Implementing Playbooks and Ansible Automation"),
         ("MODULE-8: Using Ansible's Ad-Hoc Commands and Playbooks","MODULE-8: Using Ansible's Ad-Hoc Commands and Playbooks"),
         ("MODULE-8: Managing Nodes (Servers) in Ansible","MODULE-8: Managing Nodes (Servers) in Ansible"),
         ("MODULE-8: Finding and Reusing Ansible Automation Content","MODULE-8: Finding and Reusing Ansible Automation Content"),
         ("MODULE-8: Integrating CI/CD Pipelines for Ansible Automation","MODULE-8: Integrating CI/CD Pipelines for Ansible Automation"),
         ("MODULE-8: Creating Playbooks for Automated Deployment and Configuration Tasks","MODULE-8: Creating Playbooks for Automated Deployment and Configuration Tasks"),
         ("MODULE-9: Terraform Installation and Configuration","MODULE-9: Terraform Installation and Configuration"),
         ("MODULE-9: Generating a Security Key for AWS Provider","MODULE-9: Generating a Security Key for AWS Provider"),
         ("MODULE-9: Establishing Integration with AWS Provider","MODULE-9: Establishing Integration with AWS Provider"),
         ("MODULE-9: Terraform Commands","MODULE-9: Terraform Commands"),
         ("MODULE-9: Creating an EC2 Instance Using Terraform","MODULE-9: Creating an EC2 Instance Using Terraform"),
         ("MODULE-9: Creating Resources on the AWS Provider Using Terraform","MODULE-9: Creating Resources on the AWS Provider Using Terraform"),
         ("MODULE-9: Using Terraform Templates","MODULE-9: Using Terraform Templates"),
         ("MODULE-9: Creating Terraform Source Code and Pushing to a Remote Repository","MODULE-9: Creating Terraform Source Code and Pushing to a Remote Repository"),
         ("MODULE-9: Using Terraform with Other Cloud Providers","MODULE-9: Using Terraform with Other Cloud Providers"),
         ("MODULE-9: Terraform Projects","MODULE-9: Terraform Projects"),
         ("MODULE-10: Installation and Configuration","MODULE-10: Installation and Configuration"),
         ("MODULE-10: Monitoring and Observability","MODULE-10: Monitoring and Observability"),
         ("MODULE-10: Log Management","MODULE-10: Log Management"),
         ("MODULE-10: Grafana Panel","MODULE-10: Grafana Panel"),
         ("MODULE-10: Data Sources and Dashboards","MODULE-10: Data Sources and Dashboards"),
         ("MODULE-10: Creating and Updating Dashboards and Managing Users","MODULE-10: Creating and Updating Dashboards and Managing Users"),
         ("MODULE-10: Grafana API","MODULE-10: Grafana API"),
         ("MODULE-10: Ansible Administrative Tasks","MODULE-10: Ansible Administrative Tasks"),
         ("MODULE-10: Automation and Integration with External Systems","MODULE-10: Automation and Integration with External Systems"),
         ("MODULE-10: Creating Environments and Automating Tasks","MODULE-10: Creating Environments and Automating Tasks"))



class lecture(models.Model):

  sno=models.AutoField(primary_key=True)
  username=models.ForeignKey(User,on_delete=models.CASCADE)
  heading_title=models.CharField(max_length=200, choices=htitle)
  lecture_title=models.CharField(max_length=500,choices=title)
  datetime = models.DateTimeField(default=now)

  def __str__(self):
    return str(self.username)


class zoom_session(models.Model):
  username=models.ForeignKey(User,on_delete=models.CASCADE)
  meeting_name = models.CharField(max_length=500)
  meeting_link = models.URLField(max_length=2000)
  datetime = models.DateTimeField()
  def __str__(self):
      return self.meeting_name

t=(("Monday","Monday"),("Tuesday","Tuesday"),("Wednesday","Wednesday"),("Thursday","Thursday"),("Friday","Friday"),("Saturday","Saturday"),("Sunday","Sunday"))

class timetables(models.Model):
  username = models.ForeignKey(User,on_delete=models.CASCADE)
  sno = models.AutoField(primary_key=True)
  day = models.CharField(max_length=100,choices=t)
  date = models.DateField()
  time = models.TimeField()

  def __str__(self):
      return str(self.username)
  

  
  