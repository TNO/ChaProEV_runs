import typing as ty

from ChaProEV import ChaProEV
from ETS_CookBook import ETS_CookBook as cook

if __name__ == '__main__':
    case_name = 'Mopo'
    general_parameters_file_name: str = 'ChaProEV.toml'
    profile_parameters_file_name: str = 'profile_parameters.toml'

    general_parameters: ty.Dict = cook.parameters_from_TOML(
        f'{general_parameters_file_name}'
    )

    profile_parameters: ty.Dict = cook.parameters_from_TOML(
        f'{profile_parameters_file_name}'
    )
    ChaProEV.run_ChaProEV(case_name)
