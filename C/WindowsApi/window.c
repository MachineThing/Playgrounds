#include <windows.h> // Windows API

int WINAPI WinMain(HINSTANCE hInst, HINSTANCE hPrevInst, LPSTR args, int nShowCmd) {
  MessageBox(NULL, "Hello!", "Hello there!", MB_HELP | MB_ICONINFORMATION | MB_DEFAULT_DESKTOP_ONLY);
  return 0;
}
