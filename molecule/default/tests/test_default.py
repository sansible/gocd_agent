import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_installed_packages(host):
    packages = [
        'build-essential', 'git', 'go-agent', 'python-dev', 'python-netaddr',
        'python-pip', 'python-setuptools',
    ]
    for package in packages:
        assert host.package(package).is_installed

    pip_packages = host.pip_package.get_packages()
    assert 'awscli' in pip_packages
    assert 'boto' in pip_packages


def test_files(host):
    directories = [
        '/home/go/.aws/', '/var/log/go-agent-1/', '/var/log/go-agent-2/',
    ]
    for directory in directories:
        assert host.file(directory).is_directory

    configs = [
        '/etc/default/go-agent',
        '/etc/default/go-agent-1', '/etc/default/go-agent-2',
        '/etc/init.d/go-agent-1', '/etc/init.d/go-agent-2',
        '/home/go/.aws/credentials', '/home/go/.bashrc', '/home/go/.gitconfig',
        '/home/go/.ssh/config',
    ]
    for config in configs:
        assert host.file(config).is_file

    assert host.file('/usr/share/go-agent-1').is_symlink
    assert host.file('/usr/share/go-agent-2').is_symlink
