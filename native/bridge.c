#include <CoreFoundation/CoreFoundation.h>
#include <IOKit/pwr_mgt/IOPMLib.h>
#include <stdint.h>

// Buoy 0.72's bundled framework stubs omit IOKit. Resolve it through a small
// SDK-linked bridge instead of requiring every consumer to modify its toolchain.
int32_t buoy_poweractivity_refresh(CFStringRef reason, uint32_t *assertion_id) {
    return IOPMAssertionDeclareUserActivity(reason, kIOPMUserActiveLocal, assertion_id);
}

int32_t buoy_poweractivity_release(uint32_t assertion_id) {
    return IOPMAssertionRelease(assertion_id);
}
