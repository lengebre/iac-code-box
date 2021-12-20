import json

def example_server(name: str, network:str, zone:str) -> dict:
    """ example server returns a dictionary to provision a server using terraform
    :param name: name of the server
    :param network: network to deploy server
    :param zone: zone to deploy server
    :return: terraform output for configuring a server
    """

    return {
        'resource': [
            {
                'google_compute_instance': [
                    {
                        name: [
                            {
                                'allow_stopping_for_update': True,
                                'zone': zone,
                                'boot_disk': [
                                    {
                                        'initialize_params': [
                                            {
                                                'image': 'ubuntu-1804-lts'
                                            }
                                        ]
                                    }
                                ],
                                'machine_type': 'f1-micro',
                                'name': name,
                                'network_interface': [
                                    {
                                        'network': network
                                    }
                                ],
                                'labels': {
                                    'name': name,
                                    'usage': 'iac-test-server'
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }
    
if __name__ == "__main__":
    config = example_server(name='iac-test-server', network='default', zone='us-east4-c')
    with open('main.tf.json', 'w') as outfile:
        json.dump(config, outfile, sort_keys=True, indent=4)
