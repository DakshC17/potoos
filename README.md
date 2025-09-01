# Weather Tracker

A Python application that fetches and displays current weather information for multiple cities using the WeatherAPI.com service. This project demonstrates object-oriented programming, modular design, API integration, and virtual environment usage.

##  Features

- Fetch real-time weather data for multiple cities
- Interactive command-line interface
- Modular design with separate classes and utility functions
- Error handling for network issues and invalid cities
- Formatted weather report display
- Secure API key management using environment variables

##  Project Structure

```
weather_tracker/
├── main.py              # Main application entry point
├── weather_module.py    # Weather class definition
├── weather_utils.py     # API calling functions
├── requirements.txt     # Project dependencies
├── .env                # API key configuration
└── README.md           # Project documentation
```

##  Installation & Setup

### Prerequisites
- Python 3.7 or higher
- Virtual environment (venv)
- WeatherAPI.com API key

### Steps

1. **Clone or download the project**
   ```bash
   cd weather_tracker/
   ```

2. **Activate virtual environment**
   ```bash
   source ../myvenv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API key**
   - Create a `.env` file in the project root
   - Add your WeatherAPI.com API key:
     ```
     API_KEY=your_api_key_here
     ```

## 🚀 Usage

Run the application:
```bash
python main.py
```

Follow the interactive prompts:
1. Enter city names one by one
2. Type 'done' when finished
3. View the formatted weather report

### Example Interaction

```
Enter city names (type 'done' to finish):
City: Mumbai
City: Visakhapatnam
City: Chennai
City: done

Weather Report:
Mumbai: Temp = 30.1°C, Condition = Mist, Humidity = 75%, Wind = 28.1 km/h, Last Updated = 2025-09-01 12:15
----------------------------------------------------------------------------------------------------------------------
Visakhapatnam: Temp = 30.5°C, Condition = Patchy rain nearby, Humidity = 68%, Wind = 9.4 km/h, Last Updated = 2025-09-01 12:15
----------------------------------------------------------------------------------------------------------------------
Chennai: Temp = 32.3°C, Condition = Partly cloudy, Humidity = 67%, Wind = 19.8 km/h, Last Updated = 2025-09-01 12:15
----------------------------------------------------------------------------------------------------------------------
```

## Outputs

### Sample Output - 1
![Weather Tracker Screenshot](screenshots/Screenshot%20From%202025-09-01%2012-23-20.png)

### Sample Output - 2  
![Sample Weather Report](screenshots/Screenshot%20From%202025-09-01%2012-33-19.png)

##  Architecture

### Weather Class (`weather_module.py`)
- **Purpose**: Represents weather data for a single city
- **Attributes**: city, temperature, condition, humidity, wind_speed, last_updated
- **Methods**: `__str__()` for formatted display

### Weather Utils (`weather_utils.py`)
- **Purpose**: Handles API communication
- **Function**: `fetch_weather(city)` - fetches weather data and returns Weather object
- **Features**: Error handling, API response parsing

### Main Application (`main.py`)
- **Purpose**: User interface and application flow
- **Features**: Interactive input, weather data processing, report generation

## 🔧 Technical Details

### Dependencies
- `requests`: For HTTP API calls
- `python-dotenv`: For environment variable management

### Error Handling
- Network connectivity issues
- Invalid city names
- API response errors
- Missing environment variables

### Design Patterns
- **Modular Design**: Separate files for different concerns
- **Object-Oriented**: Weather class encapsulates data and behavior
- **Error Handling**: Graceful handling of various error scenarios

## 🌐 API Integration

This project uses [WeatherAPI.com](https://www.weatherapi.com/) to fetch weather data.

### API Endpoint
```
http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no
```

### Response Data Used
- Location name
- Current temperature (Celsius)
- Weather condition
- Humidity percentage
- Wind speed (km/h)
- Last updated timestamp

##  Security

- API key stored in `.env` file (not committed to version control)
- Environment variables loaded using `python-dotenv`
- Input validation for city names

##  Testing

### Manual Testing
1. Test with valid city names
2. Test with invalid city names
3. Test network error scenarios
4. Test with empty input



##  Requirements Met

✅ Class implementation with proper attributes and methods  
✅ Modular functions in separate files  
✅ GET requests for API integration  
✅ User-defined modules  
✅ Virtual environment usage  
✅ For loops to process multiple cities  
✅ Error handling for API responses  
✅ Requirements.txt file  
✅ Clean code structure and readability  

##  Future Enhancements

- Add weather forecast functionality
- Implement data caching
- Add GUI interface
- Support for different temperature units
- Weather history tracking
- Export weather data to CSV/JSON

## 👨‍💻 Author

Daksh Choudhary


