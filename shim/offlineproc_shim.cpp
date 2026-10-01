/*
 * SPDX-FileCopyrightText: 2026 Paranoid Android
 * SPDX-License-Identifier: Apache-2.0
 */

#include <binder/IBinder.h>
#include <cutils/native_handle.h>
#include <utils/RefBase.h>

#include <vector>

namespace android {

class OfflineProcClientListener;

class OfflineProcClient {
public:
  OfflineProcClient();
  void setListener(const sp<OfflineProcClientListener> &listener);
};

OfflineProcClient::OfflineProcClient() {}

void OfflineProcClient::setListener(const sp<OfflineProcClientListener> &) {}

namespace hardware {

class IOfflineProcService : public RefBase {
public:
  static sp<IOfflineProcService> asInterface(const sp<IBinder> &binder);
};

sp<IOfflineProcService> IOfflineProcService::asInterface(const sp<IBinder> &) {
  return {};
}

class OfflineParameters {
public:
  OfflineParameters(std::vector<native_handle *>, std::vector<native_handle *>,
                    std::vector<int>, std::vector<int>);
  virtual ~OfflineParameters();
};

OfflineParameters::OfflineParameters(std::vector<native_handle *>,
                                     std::vector<native_handle *>,
                                     std::vector<int>, std::vector<int>) {}

OfflineParameters::~OfflineParameters() = default;

} // namespace hardware
} // namespace android
