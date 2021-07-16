
<h2 align='center'> Assignment - Polygon and Polygon Sequence </h3>

## Objective 1:
- Create a Polygon Class, where initializer takes in:
    - number of edges/vertices
    - circumradius

that can provide these properties:
    
    - edges
    - vertices
    - interior angle
    - edge length
    - apothem
    - area
    - perimeter
that has these functionalities:


    - a proper __repr__ function
    - implements equality (==) based on # vertices and circumradius (__eq__)
    - implements > based on number of vertices only (__gt__)



## Objective 2:
Implement a Custom Polygon sequence type, where initializer takes in:
    
    - number of vertices for largest polygon in the sequence
    - common circumradius for all polygons
that can provide these properties:

    - max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
that has these functionalities:

    - functions as a sequence type (__getitem__)
    - supports the len() function (__len__)
    - has a proper representation (__repr__)