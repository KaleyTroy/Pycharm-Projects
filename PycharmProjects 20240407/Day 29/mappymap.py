import winreg
new_value = []
current_value, _ = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Control\Keyboard Layout'), 'Scancode Map')
for index, x in enumerate(current_value):
    if index % 2: new_value[-1] += f'{x:02X}'
    else: new_value.append(f'{x:02X}')
print(new_value)
print(len(new_value))
# for g in current_value: print([f'{x:02X}'])

winreg.CloseKey(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Control\Keyboard Layout'))
