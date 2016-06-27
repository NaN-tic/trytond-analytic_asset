# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta, Pool
from trytond.model import fields

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

    @fields.depends('origin')
    def on_change_with_company(self, name=None):
        Asset = Pool().get('asset')
        try:
            company = super(AnalyticAccountEntry, self).on_change_with_company(
                name)
        except AttributeError:
            company = None
        if isinstance(self.origin, Asset):
            if self.origin.company:
                return self.origin.company.id
        return company

    @classmethod
    def search_company(cls, name, clause):
        domain = super(AnalyticAccountEntry, cls).search_company(name, clause)
        domain = ['OR',
            domain,
            [('origin.company',) + tuple(clause[1:]) + tuple(('asset',))]]
        return domain
