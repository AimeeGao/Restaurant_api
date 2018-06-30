from influxdb import InfluxDBClient
from flask import current_app

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class InfluxDB(object):

    def __init__(self, app=None):
        self.app = app
        self.influxdb = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('INFLUX_HOST', 'localhost')
        app.config.setdefault('INFLUX_PORT', '8086')
        app.config.setdefault('INFLUX_USERNAME', 'root')
        app.config.setdefault('INFLUX_PASSWORD', 'root')
        app.config.setdefault('INFLUX_DATABASE', None)

        # if hasattr(app, 'teardown_appcontext'):
        #     app.teardown_appcontext(self.teardown)
        # else:
        #     app.teardown_request(self.teardown)

    def connect(self):
        if not self.influxdb:
            self.influxdb = InfluxDBClient(
                host=current_app.config['INFLUX_HOST'],
                port=current_app.config['INFLUX_PORT'],
                username=current_app.config['INFLUX_USERNAME'],
                password=current_app.config['INFLUX_PASSWORD'],
                database=current_app.config['INFLUX_DATABASE']
            )

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'influxdb'):
            ctx.influxdb = None

    @property
    def connection(self):
        self.connect()
        return self.influxdb
        # ctx = stack.top
        # if ctx is not None:
        #     if not hasattr(ctx, 'influxdb'):
        #         ctx.influxdb = self.connect()
        #     return ctx.influxdb


influxdb = InfluxDB()
