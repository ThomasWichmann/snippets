<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	
	<xsl:output method="text" omit-xml-declaration="yes" indent="yes" encoding="UTF-8" />
	<xsl:strip-space elements="*" />

	<xsl:template match="table">
	<xsl:for-each select="row">
		<xsl:variable name="rowNumber" select="position()" />
		$<xsl:value-of select="../@name"/><xsl:value-of select="$rowNumber"/> = array(<xsl:for-each select="value|null">
			<xsl:variable name="columnNumber" select="position()" />
			'<xsl:value-of select="../../column[position() = $columnNumber]/."/>' => <xsl:choose>
		  <xsl:when test="name() = 'value'">'<xsl:value-of select="." />'</xsl:when>
		  <xsl:otherwise>
		  	<xsl:value-of select="'null'" />
		  </xsl:otherwise>
		</xsl:choose>,</xsl:for-each>
		);
	</xsl:for-each>
	
	</xsl:template>

</xsl:stylesheet>