import typing as ty

import numpy as np
import pandas as pd
from ChaProEV import ChaProEV, run_time
from ETS_CookBook import ETS_CookBook as cook


def create_profile_dataframe(
    profile_parameters: ty.Dict,
    scenario: ty.Dict,
    general_parameters: ty.Dict,
    scenario_name: str,
    case_name: str,
) -> pd.DataFrame:

    profile_dataframe: pd.DataFrame = run_time.get_time_stamped_dataframe(
        scenario, general_parameters, locations_as_columns=False
    )

    file_parameters: ty.Dict = general_parameters['files']
    output_root: str = file_parameters['output_root']
    groupfile_root: str = file_parameters['groupfile_root']
    database_folder: str = f'{output_root}/{case_name}'
    source_dataframe_path: str = (
        f'{database_folder}/{groupfile_root}_{case_name}.sqlite3'
    )
    tables_to_get: ty.List[str] = profile_parameters['tables_to_get']
    quantity_names: ty.List[str] = profile_parameters['quantity_names']
    index_is_expanded: ty.List[bool] = profile_parameters['index_is_expanded']
    base_index: ty.List[str] = profile_parameters['base_index']
    expanded_index: ty.List[str] = profile_parameters['expanded_index']

    print(source_dataframe_path)

    for table_to_get, quantity_name, table_index_is_expanded in zip(
        tables_to_get, quantity_names, index_is_expanded
    ):
        source_dataframe: pd.DataFrame = cook.read_table_from_database(
            f'{scenario_name}_{table_to_get}', source_dataframe_path
        )
        if table_index_is_expanded:
            source_dataframe = source_dataframe.set_index(expanded_index)
        else:
            source_dataframe = source_dataframe.set_index(base_index)

        quantity_values: pd.api.extensions.ExtensionArray | np.ndarray = (
            source_dataframe.sum(axis=1).values
        )

        profile_dataframe[quantity_name] = quantity_values

    return profile_dataframe


if __name__ == '__main__':
    case_name = 'Mopo'
    scenario_name = 'Netherlands_urban_car'
    general_parameters_file_name: str = 'ChaProEV.toml'
    profile_parameters_file_name: str = 'profile_parameters.toml'

    scenario: ty.Dict = cook.parameters_from_TOML(
        f'scenarios/{case_name}/{scenario_name}.toml'
    )
    general_parameters: ty.Dict = cook.parameters_from_TOML(
        f'{general_parameters_file_name}'
    )

    profile_parameters: ty.Dict = cook.parameters_from_TOML(
        f'{profile_parameters_file_name}'
    )
    ChaProEV.run_ChaProEV(case_name)

    profile: pd.DataFrame = create_profile_dataframe(
        profile_parameters,
        scenario,
        general_parameters,
        scenario_name,
        case_name,
    )
    print(profile)
