# Genesis Passive Income Bot

A containerized bot for passive income generation on cryptocurrency exchanges.

## Features

- Docker-based deployment
- Environment variable configuration
- Continuous operation with logging
- Supports multiple exchange platforms

## Prerequisites

- Docker installed on your system
- Exchange API credentials (API key and secret)
- Wallet address for receiving passive income

## Configuration

The bot uses environment variables for configuration:

- `EXCHANGE`: The name of the exchange platform
- `API`: Your API key for the exchange
- `SECRET`: Your API secret for the exchange
- `WALLET`: Your wallet address for receiving passive income

## Building the Docker Image

To build the Docker image, run:

```bash
docker build -t genesis-passive-income-bot .
```

## Running the Bot

To run the bot with your configuration:

```bash
docker run -d \
  -e EXCHANGE="your-exchange" \
  -e API="your-api-key" \
  -e SECRET="your-api-secret" \
  -e WALLET="your-wallet-address" \
  --name genesis-bot \
  genesis-passive-income-bot
```

### Example

```bash
docker run -d \
  -e EXCHANGE="binance" \
  -e API="your-api-key-here" \
  -e SECRET="your-api-secret-here" \
  -e WALLET="0x1234567890abcdef" \
  --name genesis-bot \
  genesis-passive-income-bot
```

## Viewing Logs

To view the bot's logs:

```bash
docker logs -f genesis-bot
```

## Stopping the Bot

To stop the bot:

```bash
docker stop genesis-bot
```

To remove the container:

```bash
docker rm genesis-bot
```

## File Structure

- `Dockerfile`: Docker image definition
- `manifest.json`: Input/output schema definition
- `conductor.py`: Configuration parser and main entry point
- `main.py`: Main bot logic with infinite loop
- `requirements.txt`: Python dependencies
- `config.yaml`: Generated configuration file (created at runtime)

## Development

The bot uses the following Python packages:

- `pyyaml`: For YAML configuration handling
- `aurora`: For exchange integration

## License

See LICENSE file for details.