# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta

from trytond.modules.analytic_account import AnalyticMixin

__all__ = ['Asset', 'AnalyticAccountEntry']


class Asset(AnalyticMixin):
    __name__ = 'asset'
    __metaclass__ = PoolMeta


class AnalyticAccountEntry:
    __name__ = 'analytic.account.entry'
    __metaclass__ = PoolMeta

    @classmethod
    def _get_origin(cls):
        origins = super(AnalyticAccountEntry, cls)._get_origin()
        return origins + ['asset']
