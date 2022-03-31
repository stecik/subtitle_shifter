# Subtitle Shifter
Simple CLI tool for subtitle resync

## Usage
```
subshifter [-h] [-m MIL] [-s SEC] [-M MIN] [-H HRS] input_file
```
```
subshifter subtitles.srt -M 1 -s 15 -m 500
subshifter subtitles.srt -m 1200
```

## Default behaviour

Returns .srt file resynced by given time

## Switches
### Optional switches (input required)
```
-m MIL, --mil MIL  Time for resync in milliseconds
-s SEC, --sec SEC  Time for resync in seconds
-M MIN, --min MIN  Time for resync in minutes
-H HRS, --hrs HRS  Time for resync in hours
```
### Help
```
-h, --help - Show help message
```

## How to install
### Windows
#### Option 1 (Python 3 required)
1. Download repository
2. Delete folder exe_files (only required for option 2)
3. Open cmd
4. Navigate to folder subtitle_shifter (cd path)
5. Run command python subshifter.py [-h] [-m MIL] [-s SEC] [-M MIN] [-H HRS] input_file
#### Option 2 (Python 3 not required)
1. Download repository
2. Delete folder subshifter_file (only required for option 1)
3. Navigate to C:\Users\%username%\AppData\Local
4. Create folder subshifter and copy subshifter.exe (subtitle_shifter\exe_files\subshifter.exe)
5. If using any antivirus program, add subshifter.exe as an exception (might not be necessary)
6. Add C:\Users\%username%\AppData\Local\subshifter\subshifter.exe to PATH (system environment variable)
7. Open cmd
8. Run command subshifter [-h] [-m MIL] [-s SEC] [-M MIN] [-H HRS] input_file

### Linux
#### Option 1 (Python 3 required)
1. Download repository
2. Delete folder exe_files
3. Open terminal
4. Navigate to folder dtt (cd path)
5. Run command python subshifter.py [-h] [-m MIL] [-s SEC] [-M MIN] [-H HRS] input_file
## Licence
Feel free to use/edit my software in any way possible for **_non-commercial_** purposes.
