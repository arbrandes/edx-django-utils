"""
Metrics utilities public api

See README.rst for details.
"""
from .internal.backends import DatadogBackend, NewRelicBackend, OpenTelemetryBackend, TelemetryBackend
from .internal.code_owner.middleware import CodeOwnerMonitoringMiddleware
from .internal.code_owner.utils import (
    get_code_owner_from_module,
    set_code_owner_attribute,
    set_code_owner_attribute_from_module
)
from .internal.middleware import (
    CachedCustomMonitoringMiddleware,
    CookieMonitoringMiddleware,
    DeploymentMonitoringMiddleware,
    FrontendMonitoringMiddleware,
    MonitoringMemoryMiddleware,
    MonitoringSupportMiddleware
)
from .internal.transactions import ignore_transaction
from .internal.utils import (
    accumulate,
    function_trace,
    increment,
    record_exception,
    set_custom_attribute,
    set_custom_attributes_for_course_key,
    set_monitoring_transaction_name
)
# "set_custom_metric*" methods are deprecated
from .utils import set_custom_metric, set_custom_metrics_for_course_key
