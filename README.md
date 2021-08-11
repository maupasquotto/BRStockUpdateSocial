# BRStockUpdateSocial
This is a simple scrip to post stock update in any instagram account. It checkes for holidays and weekdays before posting

## Usage
- It's recommended to create a job/cron so it can ran automatically daily
- Create a `.env` from the `.env.exemple` file & fill with the necessary info
- You'll need to provide a `ttf` since arial has copyright
- Install packages with `pip install -r requirements.txt`
- Have fun

## Docker
- Build the image `docker build -t stockupdate .`
- Run it `docker run -it --rm stockupdate`