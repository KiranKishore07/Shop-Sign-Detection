
# Shop Sign Detection

Welcome to the Shop Sign Detection project! This Python script helps you detect shop signs in videos using advanced computer vision techniques. Whether you're monitoring foot traffic in a mall or analyzing street scenes, this tool can assist you in identifying shop signs accurately.

## Features

- **AI-Powered Detection**: Leveraging cutting-edge deep learning models like YOLO and PaddleOCR, our script can detect shop signs with high accuracy.
- **Real-time Processing**: Process videos in real-time, allowing you to monitor shop signage dynamically.
- **Efficient Entry Tracking**: Automatically tracks entry and exit times for each shop, providing valuable insights into customer behavior.

## Getting Started

To get started, follow these steps:

1. **Installation**: Ensure you have Python installed on your system along with the required dependencies listed in `requirements.txt`.
   
2. **Configuration**: Update the paths to your YOLO model (`best.pt`), YouTube video link, and output Excel file in the script.

3. **Execution**: Run the `main.py` script to start processing your video and detecting shop signs.

## Requirements

- Python 3.x
- OpenCV
- Pafy
- Ultralytics YOLO
- PaddleOCR
- Pandas

## Example Usage

```python
python main.py
```

## License

This project is licensed under the [MIT License](LICENSE.md).

## Contributing

Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests.

## Acknowledgements

- Thanks to the contributors of Ultralytics YOLO and PaddleOCR for their excellent open-source projects.
- Special thanks to the Python community for their continuous support and inspiration.
