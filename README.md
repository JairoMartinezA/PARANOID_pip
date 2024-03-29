# XML AND JSON MASKING

For detailed information please visit = https://sonra.io/2019/04/01/paranoid-masking-anonymizing-and-obfuscating-pii-in-xml-and-json-data/

## About

Paranoid is data masking and obfuscation command line tool for XML and JSON file formats. Paranoid is best used in 
combination with Flexter. Flexter is Sonra's XML converter for complex XML and JSON based on industry data 
standards such as ACORD, HL7, FHIR, NDC, XBRL, FpML etc. It converts XML to any relational database, 
Hadoop formats (ORC, Parquet, Avro, Hive, Impala), or text (TSV, CSV).

## Features
* Works with one or more XML/JSON document(s). If input path points to a directory - processes its content recursively. Auto detects the format of each file.
* Masks all the elements/attributes in the XML/JSON document(s) by default while preserving the exact structure of the file(s).
* Can also mask only specific elements (by provided path/XPath) in XML/JSON document(s).
* Universal: runs on both: Python 2.6+ or 3.6+
* Offline tool - runs locally on your system. No data gets transferred anywhere.
* Open source - anyone can examine what it does to make sure the data can't be successfully de-encoded back after leaving The Sausage Machine. Any contributions are welcome!
* Easy installation - can download script itself or use `pip`


## Advanced Features
* Custom built Parser - simple parser that does only what needs to be done. Removes the overhead of using external libs. It's fast. It doesn't validate documents so can work with some rough edged ones …to some extent. 
* Smart Buffering - easy on memory (redefinable buffer to use, 512MB default) but at the same time works with huge files (eg. 10GB). Works with them even if all the content is lumped into a single line 💪‼
* Masking Statistics - Provides stats for number of xml tags and number of tags masked in during the operation which one can store in a log file too.

## Architecture
![Architecture](https://bitbucket.org/sonra/paranoid/raw/master/images/Screenshot%202019-03-28%20at%2012.23.48%20AM.png)

## Installation 

`pip install PARANOID`

# Instructions

usage: `paranoid [-h] -i INPUT [-b BYTESIZE] -o OUTPUTDIR [-l MASK] [-L LOG] [-v]`

optional arguments:
* `-h, --help`     show this help message and exit
* `-i INPUT`       Input Directory Name / File Name
*  `-b BYTESIZE`    Provide byte size to buffer
*  `-o OUTPUTDIR`   Output Directory Name
*  `-l MASK`        Input xpath or xpaths separated by ,
*  `-L LOG`         Output in Log File
*  `-v, --version`  show program's version number and exit


```
paranoid -h
```
![Usage](https://bitbucket.org/sonra/paranoid/raw/master/images/1.png?at=master)

## Usage Examples

### Mask Single File

```
paranoid -i <input filename> -o <output directory name>

```

![SingleFile](https://bitbucket.org/sonra/paranoid/raw/master/images/2.png?at=master)



### Mask all XML and JSON files in a Directory
```
paranoid -i <directory name> -o <output directory name>
```
![MultipleFile](https://bitbucket.org/sonra/paranoid/raw/master/images/3.png?at=master)

### Change Buffer size 

```
paranoid -i <File or directory name> -o <output directory name> -b buffersize
```

![BufferLimit](https://bitbucket.org/sonra/paranoid/raw/master/images/4.png?at=master)

That's the way to ingest big fat one liners as it analyses your file by streamig it byte by byte, buffer by buffer.

### Mask Certain Tags

```
paranoid -i <input filename> -o <output directory name> -l xpath separated by ,
```

![SpecificTags](https://bitbucket.org/sonra/paranoid/raw/master/images/5.png?at=master)

### Mask Certain Attributes

```
paranoid -i <input filename> -o <output directory name> -l xpath separated by ,
```

Example request:
```
python paranoid.py -i ~/tests/in/case.xml -o ~/tests/in/anonymized -b 2000 -l /Case/Id/@HubNo,/Case/ProductSet/Product/@ProductionUnit
```

This argument also accepts relative xpaths to mask nodes located at any depth of the xml tree:
```
python paranoid.py -i ~/tests/in/case.xml -o ~/tests/in/anonymized -b 2000 -l /Case/Id/@HubNo,//Product/@ProductionUnit
```

### Generate Log File

```
paranoid -i <input filename> -o <output directory name> -L Log File Location
```
![Generate Log File](https://bitbucket.org/sonra/paranoid/raw/master/images/6.png?at=master)

