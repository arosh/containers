from slackviewer.main import configure_app, app

configure_app(
    app=app,
    archive='/data/export.zip', 
    channels=None,
    no_sidebar=False,
    no_external_references=False,
    debug=False,
)
