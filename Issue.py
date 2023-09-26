[2023-09-24 06:31:24 Thread-2]   ERROR:         Traceback (most recent call last):
  File "/root/itx/src/autoreg/testworker.py", line 662, in start_tests
    self.pre_regression_reg_key_handler()
  File "/root/itx/src/autoreg/testworker.py", line 576, in pre_regression_reg_key_handler
    self.get_admin_cli().restart_ixserver(delete_ixs=True)
  File "/root/itx/lib/ssh/ixos.py", line 343, in restart_ixserver
    self.wait_for_chassis_status()
  File "/root/itx/lib/ssh/ixos.py", line 101, in wait_for_chassis_status
    IxTimer(
  File "/root/itx/lib/utils/timers.py", line 53, in start_polling
    if call_back(*args, **kwargs):
  File "/root/itx/lib/ssh/ixos.py", line 91, in wait_for_chassis_status
    chassis_ready = self.is_chassis_ready()
  File "/root/itx/lib/ssh/ixos.py", line 75, in is_chassis_ready
    if 'NOT READY' in status['Chassis status']:
KeyError: 'Chassis status'