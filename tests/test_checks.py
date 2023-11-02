import pytest
from testmodule.fileparser import JobFile, check_A, check_B, check_C, check_D, check_E

@pytest.fixture(autouse=True)
def change_test_dir(request, monkeypatch):
    monkeypatch.chdir(request.fspath.dirname)

# ===========
# CHECK_A
# ===========
def test_check_A():
    job = JobFile("A_pass.JBI")
    result = check_A(job, "W", "1")

    assert result is None

def test_check_A_errors():
    job = JobFile("A_error.JBI")
    result = check_A(job, "W", "1")

    assert result[0] == "W"
    assert result[1] == "1"
    assert result[2] == 5
    assert result[3].startswith("Every program should start with a comment line directly after the NOP statement")


# ===========
# CHECK_B
# ===========
def test_check_B():
    job = JobFile("B_pass.JBI")
    result = check_A(job, "W", "1")

    assert result is None

def test_check_B_error():
    job = JobFile("B_error.JBI")
    result = check_B(job, "W", "2")

    assert result[0] == "W"
    assert result[1] == "2"
    assert result[2] == 3
    assert result[3].startswith("The program command")
        
# ===========
# CHECK_C
# ===========
def test_check_C():
    job = JobFile("C_pass.JBI")
    result = check_C(job, "W", "3")

    assert result is None

def test_check_C_error_1():
    job = JobFile("C_error_1.JBI")
    result = check_C(job, "W", "3")

    assert result[0] == "W"
    assert result[1] == "3"
    assert result[2] == 6
    assert result[3] == "The command SET USERFRAME does not exist"

def test_check_C_error_2():
    job = JobFile("C_error_2.JBI")
    result = check_C(job, "W", "3")

    assert result[0] == "W"
    assert result[1] == "3"
    assert result[2] == 6
    assert result[3] == "The command SET USERFRAME does not exist"


def test_check_C_error_3():
    job = JobFile("C_error_3.JBI")
    result = check_C(job, "W", "3")

    assert result[0] == "W"
    assert result[1] == "3"
    assert result[2] == 7
    assert result[3] == "The command SET USERFRAME must be executed before the command CALL JOB:TRIGGER ARGF PROGRAMM_EIN is called"

def test_check_C_error_4():
    job = JobFile("C_error_4.JBI")
    result = check_C(job, "W", "3")

    assert result[0] == "W"
    assert result[1] == "3"
    assert result[2] == 7
    assert result[3] == "The command SET USERFRAME must be executed before the command CALL JOB:TRIGGER ARGF PROGRAMM_EIN is called"


# ===========
# CHECK_D
# ===========
def test_check_D():
    job = JobFile("D_pass.JBI")
    result = check_D(job, "W", "4")

    assert result is None

def test_check_D_error_1():
    job = JobFile("D_error_1.JBI")
    result = check_D(job, "W", "4")

    assert result[0][0] == "W"
    assert result[0][1] == "4"
    assert result[0][2] == 7
    assert result[0][3].startswith("When a TCPON command")

def test_check_D_error_2():
    job = JobFile("D_error_2.JBI")
    result = check_D(job, "W", "4")

    assert result[0][0] == "W"
    assert result[0][1] == "4"
    assert result[0][2] == 6
    assert result[0][3].startswith("When a TCPON command")

def test_check_D_error_3():
    job = JobFile("D_error_3.JBI")
    result = check_D(job, "W", "4")

    assert result[0][0] == "W"
    assert result[0][1] == "4"
    assert result[0][2] == 6
    assert result[0][3].startswith("When a TCPON command")

def test_check_D_error_4():
    job = JobFile("D_error_4.JBI")
    result = check_D(job, "W", "4")

    assert result[0][0] == "W"
    assert result[0][1] == "4"
    assert result[0][2] == 7
    assert result[0][3].startswith("When a TCPON command")

def test_check_D_error_5():
    job = JobFile("D_error_5.JBI")
    result = check_D(job, "W", "4")

    assert result[0][0] == "W"
    assert result[0][1] == "4"
    assert result[0][2] == 8
    assert result[0][3].startswith("When a TCPON command")

def test_check_D_error_6():
    job = JobFile("D_error_6.JBI")
    result = check_D(job, "W", "4")

    assert result[0][0] == "W"
    assert result[0][1] == "4"
    assert result[0][2] == 10
    assert result[0][3].startswith("When a TCPON command")

def test_check_D_error_7():
    job = JobFile("D_error_7.JBI")
    result = check_D(job, "W", "4")

    assert result[0][0] == "W"
    assert result[0][1] == "4"
    assert result[0][2] == 9
    assert result[0][3].startswith("When a TCPON command")

def test_check_D_error_8():
    job = JobFile("D_error_8.JBI")
    result = check_D(job, "W", "4")

    assert result[0][0] == "W"
    assert result[0][1] == "4"
    assert result[0][2] == 7
    assert result[0][3].startswith("When a TCPON command")

def test_check_D_error_9():
    job = JobFile("D_error_9.JBI")
    result = check_D(job, "W", "4")

    assert result[0][0] == "W"
    assert result[0][1] == "4"
    assert result[0][2] == 7
    assert result[0][3].startswith("When a TCPON command")

def test_check_D_error_10():
    job = JobFile("D_error_10.JBI")
    result = check_D(job, "W", "4")

    assert result[0][0] == "W"
    assert result[0][1] == "4"
    assert result[0][2] == 7
    assert result[0][3].startswith("When a TCPON command")

    assert result[0][0] == "W"
    assert result[1][1] == "4"
    assert result[1][2] == 10
    assert result[1][3].startswith("When a TCPON command")


# ===========
# CHECK_E
# ===========
def test_check_E():
    job = JobFile("E_pass.JBI")
    result = check_E(job, "W", "5")

    assert result is None

def test_check_E_error_1():
    job = JobFile("E_error_1.JBI")
    result = check_E(job, "W", "5")

    assert result[0] == "W"
    assert result[1] == "5"
    assert result[2] == None
    assert result[3].startswith("For all jobs in folder MAIN")

def test_check_E_error_2():
    job = JobFile("E_error_2.JBI")
    result = check_E(job, "W", "5")

    assert result[0] == "W"
    assert result[1] == "5"
    assert result[2] == None
    assert result[3].startswith("For all jobs in folder MAIN")


