import os
import shutil
import typing as ty

from ChaProEV import ChaProEV
from ETS_CookBook import ETS_CookBook as cook


def copy_select_files(case_name: str) -> None:
    desired_output_elements: ty.List[str] = [
        'profile_fleet',
        'weekly_consumption_table_fleet',
    ]
    select_output_folder: str = f'select_output/{case_name}/'
    cook.check_if_folder_exists(select_output_folder)
    for output_file in os.listdir(f'output/{case_name}'):
        if any(
            desired_output_element in output_file
            for desired_output_element in desired_output_elements
        ):
            if output_file.endswith('.csv'):
                shutil.copy(
                    f'output/{case_name}/{output_file}',
                    select_output_folder,
                )


if __name__ == '__main__':
    case_name: str = 'Mopo'
    ChaProEV.run_ChaProEV(case_name)

    copy_select_files(case_name)
# test use profile from net * effective effiicency (replace errors by zeros)
