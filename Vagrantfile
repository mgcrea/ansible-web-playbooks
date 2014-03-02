# -*- mode: ruby -*-
# vi: set ft=ruby :

# @cli vagrant destroy; vagrant up; sed -e 81d -i ~/.ssh/known_hosts

require 'etc'

user = Etc.getlogin
rsa_key = File.expand_path('~') + '/.ssh/id_rsa'
rsa_key_pub = File.expand_path('~') + '/.ssh/id_rsa.pub'
dsa_key = File.expand_path('~') + '/.ssh/id_dsa'
id_rsa_ssh_key_pub = File.read(File.join(Dir.home, ".ssh", "id_rsa.pub"))

if FileTest.exists?(rsa_key)
    key = rsa_key
elsif  FileTest.exists?(dsa_key)
    key = dsa_key
end

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "precise64"

  # Setting hostname
  config.vm.hostname = "precise64"

  # config.vm.provider :virtualbox do |vb|
  #   vb.customize ["modifyvm", :id, "--ioapic", "on"]
  #   vb.customize ["modifyvm", :id, "--memory", "2048"]
  #   vb.customize ["modifyvm", :id, "--cpus", "2"]
  # end

  # Set username if private ssh key exists..
  # if key
  #  config.ssh.username = user
  #  config.ssh.private_key_path = key
  # end

  config.vm.provision :shell, :inline => "echo 'Copying local id_rsa SSH Key to VM auth_keys for auth purposes (login into VM included)...' && echo '#{id_rsa_ssh_key_pub }' >> /home/vagrant/.ssh/authorized_keys && chmod 600 /home/vagrant/.ssh/authorized_keys"

  # The url from where the 'config.vm.box' box will be fetched if it
  # doesn't already exist on the user's system.
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network :forwarded_port, guest: 5099, host: 5099

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network :private_network, ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network :public_network

  # If true, then any SSH connections made will enable agent forwarding.
  # Default value: false
  # config.ssh.forward_agent = true

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider :virtualbox do |vb|
  #   # Don't boot with headless mode
  #   vb.gui = true
  #
  #   # Use VBoxManage to customize the VM. For example to change memory:
  #   vb.customize ["modifyvm", :id, "--memory", "1024"]
  # end
  #
  # View the documentation for the provider you're using for more
  # information on available options.

  # Enable provisioning with Ansible.
  #
  # config.vm.provision "ansible" do |ansible|
  #   ansible.playbook = "playbook.yml"
  #   ansible.inventory_path = "vagrant_inventory"
  # end

end
