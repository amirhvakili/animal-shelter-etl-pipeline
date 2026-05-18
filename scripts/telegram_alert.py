import requests
import datetime


def send_telegram_alert(context):
    token = "8854575715:AAGjLbtqK6-VIrxop4UAJQ0ngDgj4Bryz3U"
    chat_id = "6764714142"
    
    dag_id = context['task_instance'].dag_id
    task_id = context['task_instance'].task_id
    log_url = context['task_instance'].log_url
    exception = context.get('exception')
    
    message = (
        f"❌ *Airflow Task Failed*\n"
        f"==> Time: {datetime.datetime.now()}\n"
        f"==> DAG: {dag_id}\n"
        f"==> Task: {task_id}\n"
        f"==> Exception: {type(exception).__name__}: {exception}\n"
        f"==> Log: {log_url}"
    )
    
    
    try:
        r = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat_id, "text": message},
            verify=False,
            timeout=10
        )
        print(f"Telegram response: {r.status_code} {r.text}")
    except Exception as e:
        print(f"Telegram error: {type(e).__name__}: {e}")

