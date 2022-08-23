from app impor app
@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Country': CountryModel,
        'Region': RegionModel,
        'CountryRegion': CountryRegionModel,
    }


def main():
    app.run(debug=True, port=5001)


if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host='0.0.0.0', port=5001)
    # app.run(debug=True)
    main()
