from src.data.load_data import load_energy_data

def test_load_data(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text("Datetime,PJME_MW\n2020-01-01 00:00:00,100")

    df = load_energy_data(file)
    assert not df.empty