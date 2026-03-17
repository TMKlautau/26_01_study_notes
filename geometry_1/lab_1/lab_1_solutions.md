# Question 1

1. Construir o triângulo ABC conhecendo os lados b e c (opostos
aos vértices B e C respectivamente) e a mediana mc relativa
ao vértice C. Quantas soluções são possíveis

- solution.:

    Having b, c and mc defined.:

    ![alt text](imgs/image.png)

    We can first find the median point of the c segment by using the compass tool on both of it's endpoints, with the radius as itself.

    ![alt text](imgs/image-1.png)

    After that we can draw a segment between the 2 intersection points of the 2 newly drawn circles, we can safely define the distance of both to the ends of the segment c as the same as the lenght of c, due to they being the radius of the compass drawn circles.

    With that, the segment we just drew is the height of an equilateral triangle of side lenght c.

    And that defines H as the center point of the c segment.

    ![alt text](imgs/image-2.png)

    Again with the compass tool, we can draw 2 new circles.
    The first with radius b and center on one of the end points of the segment c, that we will call as the vertice A.
    The second with radius mc and center on the newly set, point H, the midpoint of C.

    ![alt text](imgs/image-3.png)

    The intersections of those 2, we can define as the Points I and J, can be set as the 2 possible aliases to the vertice C, as they are at a distance of A equal to the lenght b, and at lenght mc of H.

    ![alt text](imgs/image-4.png)

    With that we can define a1 and a2 as possible awnsers.

    ![alt text](imgs/image-5.png)

    Although, we can also find 4 others on an 2 dimensional plane, by swapping the vertices A and B

    <small> (need to check if that is possible, or the positions of A and B are locked based on b)</small>
---

# Question 2

2. Construir o triângulo ABC conhecendo os lados b e c (opostos
aos vértices B e C respectivamente) e a mediana ma relativa
ao vértice A.

* solution.:

    Having b, c and mc defined.:

    ![alt text](imgs/image-6.png)

    We can using only a compass and a unmarked ruler extend a segment of same lenght as ma on the same line.
    Giving us the point A'.

    ![alt text](imgs/image-7.png)

    With that, we can with the compass draw 2 circles, one of lenght b with center at A and one with lenght c with center at A', the intersection of both we can name B1 and B2.
    
    ![alt text](imgs/image-8.png)

    Doing the same, although now swapping the lenght of the circles at both centers, we can define again the intersection of those 2 circles as C1 and C2.

    ![alt text](imgs/image-9.png)

    Chosing a pair of those 4 newly set points so that the segment between the 2 intersects the segment A-A', we have a new point that we can call H.

    ![alt text](imgs/image-10.png)

    As we know, the segments A-B1 and A'-C1 being of lenght b, also with A-C1 and A'-B1 being of lenght c, we can for sure define the quadrilateral formed by those 4 points a paralelogram, as the 2 oposite sides are of equal lenght. 
    ([proof here by Opposite Sides Converse Theorem, if it's needed lol](https://study.com/skill/learn/completing-proofs-of-theorems-involving-sides-of-a-parallelogram-explanation.html#:~:text=Opposite%20Sides%20Converse%20Theorem:%20The,the%20quadrilateral%20is%20a%20parallelogram.))

    ![alt text](imgs/image-11.png)

    That makes C1-B1 and A-A' diagonals of a paralalogram, and as such they always bisect each other, and with that, H is the midpoint of B1-C1, making it of lenght a.
    As such, one of the 2 possible ABC triangle with the first defined position of A and ma is A-B1-C1.

    ![alt text](imgs/image-12.png)

    And the other one being A-B2-C2.

    ![alt text](imgs/image-13.png)

---

# Question 3

3. Prove que um raio de um círculo é perpendicular a uma corda
que não é um diâmetro se, e somente se, ele a divide em dois
segmentos congruentes.

* solution.:

    We can start by breaking the IFF proof into the 2 if->then that makes it.

    1. Prove that if a radius of a circle is perperdicular to a non diameter chord then the former bisects the later.

    2. Prove that if a radius bisects a non diameter chord then the former must be perpendicular to the later.

    Working on the 1<sup>st</sup> one.:

    We first define any chord on a circle with center A, by picking 2 random points B and C.

    ![alt text](imgs/image-14.png)

    Tracing a perpendicular line to B-C that passes on A, and definining the point D where it intersects the circle, we have the perpendicular radius A-D.
    
    (A-B-C-D is a kite tbh, the proof could just be that lol)

    ![alt text](imgs/image-15.png)

    By naming the point that the radius intersects with the chord as E, we can then build the following 2 right triangles, A-B-E and A-C-E, and due to the nature of A-B and A-C being radius, and such having lenght r, and A-E being a leg of both, we can define the lenght of C-E and B-E as $\sqrt{(AE)^2 + r^2}$, and as they are the same, AD bisects CB for sure, no matter the points B and C chosen (unless they are at the same line of A, bcs that would make it a diameter),

    ![alt text](imgs/image-16.png)

    And now for the 2<sup>nd</sup> one.: