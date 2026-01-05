# 4. To maintain State Across Methods Call: The object remember somthing form a previous method call and use it later.
# We create Python Classes when we want an object to remember information and behave differently based on past method call.

class ETLJobTracker:
    def __init__(self, job_name):
        self.job_name = job_name
        self.record_processed = 0
        self.errors = []
        self.status = "NOT_STARTED"

    def start(self):
        self.status = "RUNNING"

    def process_batch(self, record_count):
        self.record_processed += record_count

    def log_error(self, error_message):
        self.errors.append(error_message)

    def finish(self):
        self.status = "COMPLETED"

    def summary(self):
        return {
            "job": self.job_name,
            "status": self.status,
            "records": self.record_processed,
            "errors": len(self.errors)
        }


job = ETLJobTracker("battery_cell_ingestion")

job.start()
job.process_batch(1000)
job.process_batch(2000)
job.log_error("Missing voltage value")
job.finish()

print(job.summary())

# Lets write another class
class DBConnection():
    def __init__(self, connection):
        self.connection = connection
        self.transaction_active = False

    def begin(self):
        self.transaction_active = True

    def execute(self, query):
        if self.transaction_active is False:
            raise Exception("Transaction not started")
        print(f"Executing {query}")

    def commit(self):
        self.transaction_active = False


