# etcd

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/etcd) [![Testing Build](https://github.com/rolehippie/etcd/workflows/testing/badge.svg)](https://github.com/rolehippie/etcd/actions?query=workflow%3Atesting) [![Readme Build](https://github.com/rolehippie/etcd/workflows/readme/badge.svg)](https://github.com/rolehippie/etcd/actions?query=workflow%3Areadme) [![Galaxy Build](https://github.com/rolehippie/etcd/workflows/galaxy/badge.svg)](https://github.com/rolehippie/etcd/actions?query=workflow%3Agalaxy) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/etcd)](https://github.com/rolehippie/etcd/blob/master/LICENSE) 

Ansible role to install and configure etcd distributed key-value store. 

## Sponsor 

[![Proact Deutschland GmbH](https://proact.eu/wp-content/uploads/2020/03/proact-logo.png)](https://proact.eu) 

Building and improving this Ansible role have been sponsored by my employer **Proact Deutschland GmbH**.

## Table of content

* [Default Variables](#default-variables)
  * [etcd_advertise_client_address](#etcd_advertise_client_address)
  * [etcd_advertise_peer_address](#etcd_advertise_peer_address)
  * [etcd_client_address](#etcd_client_address)
  * [etcd_client_ca_cert](#etcd_client_ca_cert)
  * [etcd_client_ca_config](#etcd_client_ca_config)
  * [etcd_client_ca_key](#etcd_client_ca_key)
  * [etcd_client_cert_overwrite](#etcd_client_cert_overwrite)
  * [etcd_client_config](#etcd_client_config)
  * [etcd_client_endpoints](#etcd_client_endpoints)
  * [etcd_csr_config](#etcd_csr_config)
  * [etcd_csr_country](#etcd_csr_country)
  * [etcd_csr_location](#etcd_csr_location)
  * [etcd_csr_org](#etcd_csr_org)
  * [etcd_csr_orgunit](#etcd_csr_orgunit)
  * [etcd_csr_state](#etcd_csr_state)
  * [etcd_discovery_token](#etcd_discovery_token)
  * [etcd_peer_address](#etcd_peer_address)
  * [etcd_peer_ca_cert](#etcd_peer_ca_cert)
  * [etcd_peer_ca_config](#etcd_peer_ca_config)
  * [etcd_peer_ca_key](#etcd_peer_ca_key)
  * [etcd_peer_cert_overwrite](#etcd_peer_cert_overwrite)
  * [etcd_peer_config](#etcd_peer_config)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

## Default Variables

### etcd_advertise_client_address

Advertise client address for this host

#### Default value

```YAML
etcd_advertise_client_address: '{{ ansible_default_ipv4["address"] }}'
```

### etcd_advertise_peer_address

Advertise peer address for this host

#### Default value

```YAML
etcd_advertise_peer_address: '{{ ansible_default_ipv4["address"] }}'
```

### etcd_client_address

Client address for this host

#### Default value

```YAML
etcd_client_address: 0.0.0.0
```

### etcd_client_ca_cert

CA certificate for clients

#### Default value

```YAML
etcd_client_ca_cert:
```

### etcd_client_ca_config

Full client CA config

#### Default value

```YAML
etcd_client_ca_config:
  signing:
    default:
      expiry: 43800h
      usages:
        - signing
        - key encipherment
        - server auth
        - client auth
```

### etcd_client_ca_key

CA key for clients

#### Default value

```YAML
etcd_client_ca_key:
```

### etcd_client_cert_overwrite

Enforce new client certificates on this host

#### Default value

```YAML
etcd_client_cert_overwrite: false
```

### etcd_client_config

Client confog for SSL certy by cfssl

#### Default value

```YAML
etcd_client_config:
```

#### Example usage

```YAML
etcd_client_config:
  CN: '{{ inventory_hostname }}'
  hosts:
    - '{{ etcd_client_address }}'
    - '{{ ansible_default_ipv4["address"] }}'
    - '{{ inventory_hostname }}.example.com'
  key:
    algo: rsa
    size: 2048
```

### etcd_client_endpoints

List of client endpoints

#### Default value

```YAML
etcd_client_endpoints: []
```

### etcd_csr_config

Full config for CSR

#### Default value

```YAML
etcd_csr_config:
  CN: Etcd
  key:
    algo: rsa
    size: 2048
  names:
    - C: '{{ etcd_csr_country }}'
      ST: '{{ etcd_csr_state }}'
      L: '{{ etcd_csr_location }}'
      O: '{{ etcd_csr_org }}'
      OU: '{{ etcd_csr_orgunit }}'
```

### etcd_csr_country

Country used at etcd_csr_config

#### Default value

```YAML
etcd_csr_country:
```

### etcd_csr_location

Location used at etcd_csr_config

#### Default value

```YAML
etcd_csr_location:
```

### etcd_csr_org

Org used at etcd_csr_config

#### Default value

```YAML
etcd_csr_org:
```

### etcd_csr_orgunit

Orgunit used at etcd_csr_config

#### Default value

```YAML
etcd_csr_orgunit:
```

### etcd_csr_state

State used at etcd_csr_config

#### Default value

```YAML
etcd_csr_state:
```

### etcd_discovery_token

Discovery token for Etcd cluster

#### Default value

```YAML
etcd_discovery_token:
```

### etcd_peer_address

Peer address for this host

#### Default value

```YAML
etcd_peer_address: 0.0.0.0
```

### etcd_peer_ca_cert

CA certificate for peers

#### Default value

```YAML
etcd_peer_ca_cert:
```

### etcd_peer_ca_config

Full peer CA config

#### Default value

```YAML
etcd_peer_ca_config:
  signing:
    default:
      expiry: 43800h
      usages:
        - signing
        - key encipherment
        - server auth
        - client auth
```

### etcd_peer_ca_key

CA key for peers

#### Default value

```YAML
etcd_peer_ca_key:
```

### etcd_peer_cert_overwrite

Enforce new peer certificates on this host

#### Default value

```YAML
etcd_peer_cert_overwrite: false
```

### etcd_peer_config

Client config for SSL certs by cfssl

#### Default value

```YAML
etcd_peer_config:
```

#### Example usage

```YAML
etcd_peer_config:
  CN: '{{ inventory_hostname }}'
  hosts:
    - '{{ etcd_peer_address }}'
    - '{{ ansible_default_ipv4["address"] }}'
    - '{{ inventory_hostname }}.example.com'
  key:
    algo: rsa
    size: 2048
```

## Dependencies

* [rolehippie.cfssl](https://github.com/rolehippie/cfssl)

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
