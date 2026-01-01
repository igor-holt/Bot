import os
import sys
import yaml
import main


def parse_env_to_config():
    """Parse environment variables and write to config.yaml"""
    # Validate required environment variables
    required_vars = ['EXCHANGE', 'API', 'SECRET', 'WALLET']
    missing_vars = [var for var in required_vars if not os.environ.get(var)]
    
    if missing_vars:
        print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
        sys.exit(1)
    
    config = {
        'exchange': os.environ.get('EXCHANGE'),
        'api': os.environ.get('API'),
        'secret': os.environ.get('SECRET'),
        'wallet': os.environ.get('WALLET')
    }
    
    with open('config.yaml', 'w') as config_file:
        yaml.dump(config, config_file, default_flow_style=False)
    
    # Log configuration without exposing sensitive data
    safe_config = {k: ('***' if k in ['api', 'secret'] else v) for k, v in config.items()}
    print(f"Configuration written to config.yaml: {safe_config}")


if __name__ == "__main__":
    parse_env_to_config()
    main.main_loop()
