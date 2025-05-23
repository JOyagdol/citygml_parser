﻿<?xml version="1.0" encoding="utf-8"?>
<core:CityModel xmlns:core="http://www.opengis.net/citygml/2.0" xmlns:gen="http://www.opengis.net/citygml/generics/2.0"
  xmlns:bldg="http://www.opengis.net/citygml/building/2.0" xmlns:app="http://www.opengis.net/citygml/appearance/2.0"
  xmlns:dem="http://www.opengis.net/citygml/relief/2.0" xmlns:gml="http://www.opengis.net/gml" xmlns:xlink="http://www.w3.org/1999/xlink"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.opengis.net/citygml/building/2.0 http://schemas.opengis.net/citygml/building/2.0/building.xsd http://www.opengis.net/citygml/appearance/2.0 http://schemas.opengis.net/citygml/appearance/2.0/appearance.xsd http://www.opengis.net/citygml/relief/2.0 http://schemas.opengis.net/citygml/relief/2.0/relief.xsd http://www.opengis.net/citygml/2.0 http://schemas.opengis.net/citygml/2.0/cityGMLBase.xsd http://www.opengis.net/citygml/generics/2.0 http://schemas.opengis.net/citygml/generics/2.0/generics.xsd">

  <!--
Einfaches Gebäude mit Grundriss 3m x 5m und Satteldach, Traufhöhe 3m, Firsthöhe 4,5m
Modelliert mit Begrenzungsflächen (eine Dachfläche, 4 Wandflächen, 1 Grundfläche), 
die Gebäudegeometrie als Solid, der auf die Polygone der Begrenzungsflächen referenziert 

CityGML 2.0

Gebäudevolumen: 56,25 m3

10.5.2017

Author: V. Coors, HFT Stuttgart
Lizenz: 
-->

  <core:cityObjectMember>
    <bldg:Building gml:id="_Simple_BD.1">
      <bldg:lod2Solid>
        <gml:Solid>
          <gml:exterior>
            <gml:CompositeSurface>
              <gml:surfaceMember xlink:href="#_Simple_BD.1_PG.1"/>
              <gml:surfaceMember xlink:href="#_Simple_BD.1_PG.2"/>
              <gml:surfaceMember xlink:href="#_Simple_BD.1_PG.3"/>
              <gml:surfaceMember xlink:href="#_Simple_BD.1_PG.4"/>
              <gml:surfaceMember xlink:href="#_Simple_BD.1_PG.5"/>
              <gml:surfaceMember xlink:href="#_Simple_BD.1_PG.6"/>
              <gml:surfaceMember xlink:href="#_Simple_BD.1_PG.7"/>
            </gml:CompositeSurface>
          </gml:exterior>
        </gml:Solid>
      </bldg:lod2Solid>
      <bldg:boundedBy>
        <bldg:WallSurface gml:id="_Simple_BD.1_WallSurface_1">
          <bldg:lod2MultiSurface>
            <gml:MultiSurface>
              <gml:surfaceMember>
                <gml:Polygon gml:id="_Simple_BD.1_PG.2">
                  <gml:exterior>
                    <gml:LinearRing gml:id="_Simple_BD.1_PG.2_LR.1">
                      <gml:posList srsDimension="3"> 13.0 15.0 0.0 13.0 15.0 3.0 13.0 10.0 3.0 13.0 10.0 0.0 13.0 15.0 0.0 </gml:posList>
                    </gml:LinearRing>
                  </gml:exterior>
                </gml:Polygon>
              </gml:surfaceMember>
            </gml:MultiSurface>
          </bldg:lod2MultiSurface>
        </bldg:WallSurface>
      </bldg:boundedBy>
      <bldg:boundedBy>
        <bldg:WallSurface gml:id="_Simple_BD.1_WallSurface_2">
          <bldg:lod2MultiSurface>
            <gml:MultiSurface>
              <gml:surfaceMember>
                <gml:Polygon gml:id="_Simple_BD.1_PG.3">
                  <gml:exterior>
                    <gml:LinearRing gml:id="_Simple_BD.1_PG.3_LR.1">
                      <gml:posList srsDimension="3"> 10.0 15.0 0.0 10.0 15.0 3.0 11.5 15.0 4.5 13.0 15.0 3.0 13.0 15.0 0.0 10.0 15.0 0.0
                      </gml:posList>
                    </gml:LinearRing>
                  </gml:exterior>
                </gml:Polygon>
              </gml:surfaceMember>
            </gml:MultiSurface>
          </bldg:lod2MultiSurface>
        </bldg:WallSurface>
      </bldg:boundedBy>
      <bldg:boundedBy>
        <bldg:WallSurface gml:id="_Simple_BD.1_WallSurface_3">
          <bldg:lod2MultiSurface>
            <gml:MultiSurface>
              <gml:surfaceMember>
                <gml:Polygon gml:id="_Simple_BD.1_PG.4">
                  <gml:exterior>
                    <gml:LinearRing gml:id="_Simple_BD.1_PG.4_LR.1">
                      <gml:posList srsDimension="3"> 10.0 10.0 3.0 10.0 15.0 3.0 10.0 15.0 0.0 10.0 10.0 0.0 10.0 10.0 3.0 </gml:posList>
                    </gml:LinearRing>
                  </gml:exterior>
                </gml:Polygon>
              </gml:surfaceMember>
            </gml:MultiSurface>
          </bldg:lod2MultiSurface>
        </bldg:WallSurface>
      </bldg:boundedBy>
      <bldg:boundedBy>
        <bldg:WallSurface gml:id="_Simple_BD.1_WallSurface_4">
          <bldg:lod2MultiSurface>
            <gml:MultiSurface>
              <gml:surfaceMember>
                <gml:Polygon gml:id="_Simple_BD.1_PG.5">
                  <gml:exterior>
                    <gml:LinearRing gml:id="_Simple_BD.1_PG.5_LR.1">
                      <gml:posList srsDimension="3"> 13.0 10.0 0.0 13.0 10.0 3.0 11.5 10.0 4.5 10.0 10.0 3.0 10.0 10.0 0.0 13.0 10.0 0.0
                      </gml:posList>
                    </gml:LinearRing>
                  </gml:exterior>
                </gml:Polygon>
              </gml:surfaceMember>
            </gml:MultiSurface>
          </bldg:lod2MultiSurface>
        </bldg:WallSurface>
      </bldg:boundedBy>
      <bldg:boundedBy>
        <bldg:RoofSurface gml:id="_Simple_BD.1_RoofSurface_1">
          <bldg:lod2MultiSurface>
            <gml:MultiSurface>
              <gml:surfaceMember>
                <gml:Polygon gml:id="_Simple_BD.1_PG.6">
                  <gml:exterior>
                    <gml:LinearRing gml:id="_Simple_BD.1_PG.6_LR.1">
                      <gml:posList srsDimension="3"> 10.0 10.0 3.0 11.5 10.0 4.5 11.5 15.0 4.5 10.0 15.0 3.0 10.0 10.0 3.0 </gml:posList>
                    </gml:LinearRing>
                  </gml:exterior>
                </gml:Polygon>
              </gml:surfaceMember>
              <gml:surfaceMember>
                <gml:Polygon gml:id="_Simple_BD.1_PG.7">
                  <gml:exterior>
                    <gml:LinearRing gml:id="_Simple_BD.1_PG.7_LR.1">
                      <gml:posList srsDimension="3"> 11.5 10.0 4.5 13.0 10.0 3.0 13.0 15.0 3.0 11.5 15.0 4.5 11.5 10.0 4.5 </gml:posList>
                    </gml:LinearRing>
                  </gml:exterior>
                </gml:Polygon>
              </gml:surfaceMember>
            </gml:MultiSurface>
          </bldg:lod2MultiSurface>
        </bldg:RoofSurface>
      </bldg:boundedBy>
      <bldg:boundedBy>
        <bldg:GroundSurface gml:id="_Simple_BD.1_GroundSurface_1">
          <bldg:lod2MultiSurface>
            <gml:MultiSurface>
              <gml:surfaceMember>
                <gml:Polygon gml:id="_Simple_BD.1_PG.1">
                  <gml:exterior>
                    <gml:LinearRing gml:id="_Simple_BD.1_PG.1_LR.1">
                      <gml:posList srsDimension="3"> 10.0 10.0 0.0 10.0 15.0 0.0 13.0 15.0 0.0 13.0 10.0 0.0 10.0 10.0 0.0 </gml:posList>
                    </gml:LinearRing>
                  </gml:exterior>
                </gml:Polygon>
              </gml:surfaceMember>
            </gml:MultiSurface>
          </bldg:lod2MultiSurface>
        </bldg:GroundSurface>
      </bldg:boundedBy>
    </bldg:Building>
  </core:cityObjectMember>
</core:CityModel>
