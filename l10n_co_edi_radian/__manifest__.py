{
    "name": "Colombia EDI RADIAN Events - Stub",
    "version": "18.0.1.0.0",
    "category": "Accounting/Localizations",
    "summary": "RADIAN events (send/receive/sync) - stub.",
    "author": "andradevidarte",
    "license": "LGPL-3",
    "depends": ["l10n_co_edi_base"],
    "data": [
        "security/ir.model.access.csv",
        "views/radian_event_views.xml",
        "data/cron.xml",
    ],
    "installable": True,
}
