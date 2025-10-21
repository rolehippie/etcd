import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_etcd_is_installed(host):
    etcd = host.package("etcd-server")
    assert etcd.is_installed
