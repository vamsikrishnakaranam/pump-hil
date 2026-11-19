#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_chip_info.h"

void app_main(void)
{
    esp_chip_info_t info;
    esp_chip_info(&info);
    printf("Hello world! pump-hil board check: ESP32 with %d cores\n", info.cores);

    for (int i = 0; ; i++) {
        printf("tick %d\n", i);
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}
