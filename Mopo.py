from ChaProEV import ChaProEV


def create_output(case_name: str) -> None:
    pass


if __name__ == '__main__':
    case_name = 'Mopo'
    ChaProEV.run_ChaProEV(case_name)
    create_output(case_name)
