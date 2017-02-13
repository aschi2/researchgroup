<?php
$this->client =
    new SoapClient(
        'http://weather.gov/forecasts/xml/SOAP_server/ndfdXMLserver.php?wsdl',
        array('cache_wsdl'=>WSDL_CACHE_NONE)
    );
    class weatherParameters {
        function weatherParameters() {
            $this->maxt     = false;    $this->mint     = false;
            $this->temp     = true;     $this->dew          = true;
            $this->pop12        = true;     $this->qpf          = true;
            $this->sky          = true;     $this->snow     = true;
            $this->wspd     = true;     $this->wdir     = true;
            $this->wx           = false;    $this->waveh        = false;
            $this->icons        = true;     $this->rh           = true;
            $this->appt     = true;     $this->incw34       = false;
            $this->incw50       = false;    $this->incw64       = false;
            $this->cumw34       = false;    $this->cumw50       = false;
            $this->cumw64       = false;    $this->critfireo    = false;
            $this->dryfireo = false;    $this->conhazo      = false;
            $this->ptornado = false;    $this->phail        = false;
            $this->ptstmwinds   = false;    $this->pxtornado    = false;
            $this->pxhail       = false;    $this->pxtstmwinds  = false;
            $this->ptotsvrtstm  = false;    $this->pxtotsvrtstm= false;
            $this->tmpabv14d    = false;    $this->tmpblw14d    = false;
            $this->tmpabv30d    = false;    $this->tmpblw30d    = false;
            $this->tmpabv90d    = false;    $this->tmpblw90d    = false;
            $this->prcpabv14d   = false;    $this->prcpblw14d   = false;
            $this->prcpabv30d   = false;    $this->prcpblw30d   = false;
            $this->prcpabv90d   = false;    $this->prcpblw90d   = false;
            $this->precipa_r    = true;     $this->sky_r        = true;
            $this->temp_r       = true;     $this->td_r     = true;
            $this->wdir_r       = true;     $this->wspd_r       = true;
            $this->wwa          = true;     $this->wgust        = true;
        }
      };
$wParameters = new weatherParameters();
$weatherParameters = new SoapVar(
    // object to convert,encoding,name to give the object, name space definition
    $wParameters, SOAP_ENC_OBJECT, 'weatherParameters', 'http://graphical.weather.gov/xml/DWMLgen/wsdl/ndfdXML.wsdl'
);
$this->xml =
    $this->client->NDFDgen(
        new SoapParam($this->latitude,  'latitude'),
        new SoapParam($this->longitude,'longitude'),
        new SoapParam('time-series',   'product'),
        new SoapParam($startTime,       'startTime'),
        new SoapParam($endTime,     'startTime'),
        new SoapParam('e',             'Unit'),
        new SoapParam($weatherParameters,'weatherParameters'
        )
    );
?>
