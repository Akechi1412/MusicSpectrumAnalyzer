/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2023 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "usb_device.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include <string.h>
#include "usbd_cdc_if.h"
/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */
typedef struct {
	uint8_t red;
	uint8_t green;
	uint8_t blue;
} Color_t;
/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
#define 	CDC_BUFFER_SIZE 		8
#define 	ROW_SIZE 				8
#define 	COL_SIZE				8
#define		BIT_NUM					8
#define		RGB_NUM					3
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
SPI_HandleTypeDef hspi1;

TIM_HandleTypeDef htim2;

/* USER CODE BEGIN PV */
uint8_t RX_buffer[APP_RX_DATA_SIZE];
uint8_t SPI_buffer[ROW_SIZE][BIT_NUM][RGB_NUM];
Color_t primary_color;
Color_t secondary_color;
Color_t tertiary_color;
uint8_t bit_index;
uint8_t row;

const uint8_t TIMER_SCALER[BIT_NUM] = {0, 1, 3, 7, 15, 31, 63, 127};
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_TIM2_Init(void);
static void MX_SPI1_Init(void);
/* USER CODE BEGIN PFP */
static void RGBLedMatrix_Init(void);
static void RGBLedMatrix_Display(uint8_t mode, uint8_t* magnitude_levels);
static void RGBLedMatrix_Scan(uint8_t row);
static void RGBLedMatrix_ShiftOut(uint8_t* data, uint8_t size);
static void CDC_ReceivedCallback();
/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_TIM2_Init();
  MX_USB_DEVICE_Init();
  MX_SPI1_Init();
  /* USER CODE BEGIN 2 */
  RGBLedMatrix_Init();
  HAL_TIM_Base_Start_IT(&htim2);
  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
	  if (RX_buffer[0] != '\0') {
		  CDC_ReceivedCallback();
//		  CDC_Transmit_FS(RX_buffer, CDC_BUFFER_SIZE);
		  memset(RX_buffer, '\0', sizeof(RX_buffer));
	  }
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};
  RCC_PeriphCLKInitTypeDef PeriphClkInit = {0};

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.HSEPredivValue = RCC_HSE_PREDIV_DIV1;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL9;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
  {
    Error_Handler();
  }
  PeriphClkInit.PeriphClockSelection = RCC_PERIPHCLK_USB;
  PeriphClkInit.UsbClockSelection = RCC_USBCLKSOURCE_PLL_DIV1_5;
  if (HAL_RCCEx_PeriphCLKConfig(&PeriphClkInit) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief SPI1 Initialization Function
  * @param None
  * @retval None
  */
static void MX_SPI1_Init(void)
{

  /* USER CODE BEGIN SPI1_Init 0 */

  /* USER CODE END SPI1_Init 0 */

  /* USER CODE BEGIN SPI1_Init 1 */

  /* USER CODE END SPI1_Init 1 */
  /* SPI1 parameter configuration*/
  hspi1.Instance = SPI1;
  hspi1.Init.Mode = SPI_MODE_MASTER;
  hspi1.Init.Direction = SPI_DIRECTION_2LINES;
  hspi1.Init.DataSize = SPI_DATASIZE_8BIT;
  hspi1.Init.CLKPolarity = SPI_POLARITY_LOW;
  hspi1.Init.CLKPhase = SPI_PHASE_1EDGE;
  hspi1.Init.NSS = SPI_NSS_SOFT;
  hspi1.Init.BaudRatePrescaler = SPI_BAUDRATEPRESCALER_4;
  hspi1.Init.FirstBit = SPI_FIRSTBIT_LSB;
  hspi1.Init.TIMode = SPI_TIMODE_DISABLE;
  hspi1.Init.CRCCalculation = SPI_CRCCALCULATION_DISABLE;
  hspi1.Init.CRCPolynomial = 10;
  if (HAL_SPI_Init(&hspi1) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN SPI1_Init 2 */

  /* USER CODE END SPI1_Init 2 */

}

/**
  * @brief TIM2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_TIM2_Init(void)
{

  /* USER CODE BEGIN TIM2_Init 0 */

  /* USER CODE END TIM2_Init 0 */

  TIM_ClockConfigTypeDef sClockSourceConfig = {0};
  TIM_MasterConfigTypeDef sMasterConfig = {0};

  /* USER CODE BEGIN TIM2_Init 1 */

  /* USER CODE END TIM2_Init 1 */
  htim2.Instance = TIM2;
  htim2.Init.Prescaler = 1-1;
  htim2.Init.CounterMode = TIM_COUNTERMODE_UP;
  htim2.Init.Period = 288-1;
  htim2.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
  htim2.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE;
  if (HAL_TIM_Base_Init(&htim2) != HAL_OK)
  {
    Error_Handler();
  }
  sClockSourceConfig.ClockSource = TIM_CLOCKSOURCE_INTERNAL;
  if (HAL_TIM_ConfigClockSource(&htim2, &sClockSourceConfig) != HAL_OK)
  {
    Error_Handler();
  }
  sMasterConfig.MasterOutputTrigger = TIM_TRGO_RESET;
  sMasterConfig.MasterSlaveMode = TIM_MASTERSLAVEMODE_DISABLE;
  if (HAL_TIMEx_MasterConfigSynchronization(&htim2, &sMasterConfig) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN TIM2_Init 2 */

  /* USER CODE END TIM2_Init 2 */

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};
/* USER CODE BEGIN MX_GPIO_Init_1 */
/* USER CODE END MX_GPIO_Init_1 */

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOD_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_2|GPIO_PIN_3
                          |GPIO_PIN_6, GPIO_PIN_RESET);

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOB, GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_10|GPIO_PIN_11, GPIO_PIN_RESET);

  /*Configure GPIO pins : PA0 PA1 PA2 PA3
                           PA6 */
  GPIO_InitStruct.Pin = GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_2|GPIO_PIN_3
                          |GPIO_PIN_6;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  /*Configure GPIO pins : PB0 PB1 PB10 PB11 */
  GPIO_InitStruct.Pin = GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_10|GPIO_PIN_11;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

/* USER CODE BEGIN MX_GPIO_Init_2 */
/* USER CODE END MX_GPIO_Init_2 */
}

/* USER CODE BEGIN 4 */
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim) {
	__HAL_TIM_SET_PRESCALER(htim, TIMER_SCALER[bit_index]);
	htim->Instance->EGR = TIM_EGR_UG;
	__HAL_TIM_CLEAR_IT(htim, TIM_IT_UPDATE);

	if (bit_index == 0) {
		RGBLedMatrix_Scan(8);
	}
	RGBLedMatrix_ShiftOut(SPI_buffer[row][bit_index], 3);
	if (bit_index == 0) {
		RGBLedMatrix_Scan(row);
	}

	bit_index++;
	if (bit_index == BIT_NUM) {
		bit_index = 0;
		row++;
		if (row == ROW_SIZE) row = 0;
	}
}

static void RGBLedMatrix_Init(void) {
	row = 0;
	bit_index = 0;

	memset(SPI_buffer, 0xFF, sizeof(SPI_buffer));

	primary_color.red = 0x1E;
	primary_color.green = 0x81;
	primary_color.blue = 0xB0;

	secondary_color.red = 0x6C;
	secondary_color.green = 0x25;
	secondary_color.blue = 0xBE;

	tertiary_color.red = 0xBE;
	tertiary_color.green = 0xA9;
	tertiary_color.blue = 0x25;
}

static void RGBLedMatrix_Scan(uint8_t row) {
	HAL_GPIO_WritePin(GPIOA, GPIO_PIN_0, 0);
	HAL_GPIO_WritePin(GPIOA, GPIO_PIN_1, 0);
	HAL_GPIO_WritePin(GPIOA, GPIO_PIN_2, 0);
	HAL_GPIO_WritePin(GPIOA, GPIO_PIN_3, 0);
	HAL_GPIO_WritePin(GPIOB, GPIO_PIN_11, 0);
	HAL_GPIO_WritePin(GPIOB, GPIO_PIN_10, 0);
	HAL_GPIO_WritePin(GPIOB, GPIO_PIN_1, 0);
	HAL_GPIO_WritePin(GPIOB, GPIO_PIN_0, 0);

	switch(row) {
	case 0:
		HAL_GPIO_WritePin(GPIOA, GPIO_PIN_0, 1);
		break;
	case 1:
		HAL_GPIO_WritePin(GPIOA, GPIO_PIN_1, 1);
		break;
	case 2:
		HAL_GPIO_WritePin(GPIOA, GPIO_PIN_2, 1);
		break;
	case 3:
		HAL_GPIO_WritePin(GPIOA, GPIO_PIN_3, 1);
		break;
	case 4:
		HAL_GPIO_WritePin(GPIOB, GPIO_PIN_11, 1);
		break;
	case 5:
		HAL_GPIO_WritePin(GPIOB, GPIO_PIN_10, 1);
		break;
	case 6:
		HAL_GPIO_WritePin(GPIOB, GPIO_PIN_1, 1);
		break;
	case 7:
		HAL_GPIO_WritePin(GPIOB, GPIO_PIN_0, 1);
		break;
	}
}

static void RGBLedMatrix_ShiftOut(uint8_t* data, uint8_t size) {
	HAL_GPIO_WritePin(GPIOA, GPIO_PIN_6, 0);
	HAL_SPI_Transmit(&hspi1, data, size, 1);
	HAL_GPIO_WritePin(GPIOA, GPIO_PIN_6, 1);
}

static void RGBLedMatrix_Display(uint8_t mode, uint8_t* magnitude_levels) {
	uint8_t mark;
	uint8_t marks[ROW_SIZE];
	uint8_t i, j;

	for (i = 0; i < ROW_SIZE; i++) {
		marks[ROW_SIZE - 1 - i] = 0x00;
		for (j = 0; j < COL_SIZE; j++) {
			mark = i < magnitude_levels[j] ? 0 : 1;
			marks[ROW_SIZE - 1 - i] |= (mark << (7 - j));
		}
	}

	switch(mode) {
	case 1:
		for (i = 0; i < ROW_SIZE; i++){
			for (j = 0; j < BIT_NUM; j++) {
				if ((primary_color.blue >> j) & 0x01) {
					SPI_buffer[i][j][0] =  marks[i];
				}
				else {
					SPI_buffer[i][j][0] = 0xFF;
				}

				if ((primary_color.green >> j) & 0x01) {
					SPI_buffer[i][j][1] =  marks[i];
				}
				else {
					SPI_buffer[i][j][1] = 0xFF;
				}

				if ((primary_color.red >> j) & 0x01) {
					SPI_buffer[i][j][2] =  marks[i];
				}
				else {
					SPI_buffer[i][j][2] = 0xFF;
				}
			}
		}
		break;
	case 2:
		for (i = 0; i < ROW_SIZE / 2; i++){
			for (j = 0; j < BIT_NUM; j++) {
				if ((secondary_color.blue >> j) & 0x01) {
					SPI_buffer[i][j][0] =  marks[i];
				}
				else {
					SPI_buffer[i][j][0] = 0xFF;
				}

				if ((secondary_color.green >> j) & 0x01) {
					SPI_buffer[i][j][1] =  marks[i];
				}
				else {
					SPI_buffer[i][j][1] = 0xFF;
				}

				if ((secondary_color.red >> j) & 0x01) {
					SPI_buffer[i][j][2] =  marks[i];
				}
				else {
					SPI_buffer[i][j][2] = 0xFF;
				}
			}
		}
		for (i = ROW_SIZE / 2; i < ROW_SIZE; i++){
			for (j = 0; j < BIT_NUM; j++) {
				if ((primary_color.blue >> j) & 0x01) {
					SPI_buffer[i][j][0] =  marks[i];
				}
				else {
					SPI_buffer[i][j][0] = 0xFF;
				}

				if ((primary_color.green >> j) & 0x01) {
					SPI_buffer[i][j][1] =  marks[i];
				}
				else {
					SPI_buffer[i][j][1] = 0xFF;
				}

				if ((primary_color.red >> j) & 0x01) {
					SPI_buffer[i][j][2] =  marks[i];
				}
				else {
					SPI_buffer[i][j][2] = 0xFF;
				}
			}
		}
		break;
	case 3:
		for (i = 0; i < ROW_SIZE / 3; i++){
			for (j = 0; j < BIT_NUM; j++) {
				if ((tertiary_color.blue >> j) & 0x01) {
					SPI_buffer[i][j][0] =  marks[i];
				}
				else {
					SPI_buffer[i][j][0] = 0xFF;
				}

				if ((tertiary_color.green >> j) & 0x01) {
					SPI_buffer[i][j][1] =  marks[i];
				}
				else {
					SPI_buffer[i][j][1] = 0xFF;
				}

				if ((tertiary_color.red >> j) & 0x01) {
					SPI_buffer[i][j][2] =  marks[i];
				}
				else {
					SPI_buffer[i][j][2] = 0xFF;
				}
			}
		}
		for (i = ROW_SIZE / 3; i <= ROW_SIZE / 2; i++){
			for (j = 0; j < BIT_NUM; j++) {
				if ((secondary_color.blue >> j) & 0x01) {
					SPI_buffer[i][j][0] =  marks[i];
				}
				else {
					SPI_buffer[i][j][0] = 0xFF;
				}

				if ((secondary_color.green >> j) & 0x01) {
					SPI_buffer[i][j][1] =  marks[i];
				}
				else {
					SPI_buffer[i][j][1] = 0xFF;
				}

				if ((secondary_color.red >> j) & 0x01) {
					SPI_buffer[i][j][2] =  marks[i];
				}
				else {
					SPI_buffer[i][j][2] = 0xFF;
				}
			}
		}
		for (i = ROW_SIZE / 2 + 1; i < ROW_SIZE; i++){
			for (j = 0; j < BIT_NUM; j++) {
				if ((primary_color.blue >> j) & 0x01) {
					SPI_buffer[i][j][0] =  marks[i];
				}
				else {
					SPI_buffer[i][j][0] = 0xFF;
				}

				if ((primary_color.green >> j) & 0x01) {
					SPI_buffer[i][j][1] =  marks[i];
				}
				else {
					SPI_buffer[i][j][1] = 0xFF;
				}

				if ((primary_color.red >> j) & 0x01) {
					SPI_buffer[i][j][2] =  marks[i];
				}
				else {
					SPI_buffer[i][j][2] = 0xFF;
				}
			}
		}
		break;
	}
}

static void CDC_ReceivedCallback() {
	uint8_t byte;
	uint8_t magnitude_levels[8];
	uint8_t mode;
	uint8_t color_type;
	Color_t color;
	uint8_t i;

	for (i = 0; i < CDC_BUFFER_SIZE; i++) {
		byte = RX_buffer[i];
		switch(i) {
		case 0:
			mode = byte >> 4;
			color_type = byte & 0x0F;
			break;
		case 1:
			magnitude_levels[0] = byte >> 4;
			magnitude_levels[1] = byte & 0x0F;
			break;
		case 2:
			magnitude_levels[2] = byte >> 4;
			magnitude_levels[3] = byte & 0x0F;
			break;
		case 3:
			magnitude_levels[4] = byte >> 4;
			magnitude_levels[5] = byte & 0x0F;
			break;
		case 4:
			magnitude_levels[6] = byte >> 4;
			magnitude_levels[7] = byte & 0x0F;
			break;
		case 5:
			color.red = byte;
			break;
		case 6:
			color.green = byte;
			break;
		case 7:
			color.blue = byte;
			break;
		}
	}

	switch(color_type) {
	case 1:
		primary_color.red = color.red;
		primary_color.green = color.green;
		primary_color.blue = color.blue;
		break;
	case 2:
		secondary_color.red = color.red;
		secondary_color.green = color.green;
		secondary_color.blue = color.blue;
		break;
	case 3:
		tertiary_color.red = color.red;
		tertiary_color.green = color.green;
		tertiary_color.blue = color.blue;
		break;
	}

	RGBLedMatrix_Display(mode, magnitude_levels);
}
/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
