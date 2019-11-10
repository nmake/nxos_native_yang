# NXOS native yang

This is an Ansible role used to push and pull the configuration from nexus devices using netconf and the nx-os native yang model.

No working knowledge of netconf or yang is necessary.

## Prerequisits

- netconf enabled on the device
- ncclient installed

The role provide a number actions shown below:

## Show the supported resources available for a given device

```yaml

- name: Show all the available resources for this device
  include_role:
    name: nxos_native_yang
  vars:
    action: get_available_resources

TASK [nxos_native_yang : Show the available resources] ************************
ok: [nxos101] =>
  nxos_native_yang['available_resources']:
  - acct-items
  - acl-items
  - acllog-items
  - action-items
  - actrl-items
  - actrlcapprov-items
  - adjacency-items
  - analytics-items
  - arp-items
  - bd-items
  <...>
```

## Show a sample data structure for a given resource

```yaml
- name: Show the sample data structure for a resource
  include_role:
    name: nxos_native_yang
  vars:
    action: get_samples
    resources:
    - vtp-items

TASK [nxos_native_yang : Show the samples] ************************************
ok: [nxos101] =>
  samples:
    vtp-items:
      inst-items:
        ctrl: null
        domain: null
        name: null
        operErr: null
        password: null
      name: null
      operErr: null
```

## Gather facts for specific resources

```yaml
- name: Gather facts for specifc resources
  include_role:
    name: nxos_native_yang
  vars:
    action: gather_facts
    resources:
    - bd-items
    - intf-items

  TASK [debug] ****************************************************************
  ok: [nxos101] =>
    native_yang_facts:
      bd-items:
        bd-items:
          BD-list:
          - BdState: active
            adminSt: active
            bridgeMode: mac
            fabEncap: vlan-42
            fwdCtrl: mdst-flood
            fwdMode: bridge,route
            id: '42'
            mode: CE
            name: ffffff
            xConnect: disable
            <...>
      intf-items:
        phys-items:
          PhysIf-list:
          - FECMode: auto
            accessVlan: vlan-1
            adminSt: up
            autoNeg: 'on'
            beacon: 'off'
            bw: '0'
            controllerId: null
            delay: '1'
            dot1qEtherType: '0x8100'
            duplex: auto
            eeep-items:
              eeeLat: variable
              eeeLpi: aggressive
              eeeState: not-applicable
            id: eth1/71
            <...>
```

## Build an inventory for all resources available

```yaml

- name: Generate an inventory file entry for the given resources
  include_role:
    name: nxos_native_yang
  vars:
    action: generate_inventory
    inventory_path: "./inventory/host_vars/{{ inventory_hostname }}"
    resources:
    - all
    - '!acl-items'


$ tree inventory
inventory
|-- host_vars
|   `-- nxos101
|       |-- acct-items.yaml
|       |-- acllog-items.yaml
|       |-- action-items.yaml
|       |-- actrlcapprov-items.yaml
|       |-- actrl-items.yaml
|       |-- adjacency-items.yaml
|       |-- analytics-items.yaml
|       |-- arp-items.yaml
|       |-- bd-items.yaml
|       |-- bdTable-items.yaml
|       |-- bfd-items.yaml
|       |-- bgp-items.yaml
|       |-- boot-items.yaml

```

## Apply configuration to the device

```yaml

- name: Apply configuration to the device
  include_role:
    name: nxos_native_yang
  vars:
    action: apply_configuration
    check_mode: True
    resources:
    - name: "bd-items"
      config: "{{ hostvars[inventory_hostname]['bd-items'] }}"
    - name: "intf-items"
      config: "{{ hostvars[inventory_hostname]['intf-items'] }}"
```
