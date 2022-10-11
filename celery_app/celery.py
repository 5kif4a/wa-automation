from celery import Celery

app = Celery('wa-automation',
             broker='redis://localhost:6379',
             include=['celery_app.tasks'])

if __name__ == '__main__':
    app.start()
