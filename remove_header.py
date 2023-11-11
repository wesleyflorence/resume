#!/usr/bin/env python3

import panflute as pf

def action(elem, doc):
    if isinstance(elem, pf.Table):
        content = pf.stringify(elem)
        if 'Email :' in content and 'Mobile :' in content:
            return []  # Return an empty list to remove this element

        # This function will create a Para that contains two Spans for organization and location
        def create_combined_para(organization_text, location_text):
            organization_span = pf.Span(pf.Str(organization_text), classes=['resume-organization'])
            location_span = pf.Span(pf.Str(location_text), classes=['resume-location'])
            return pf.Para(organization_span, pf.Space(), location_span)

        divs = []
        for row in elem.content:
            if len(row.content) >= 2:
                cells = row.content

                # Extract organization and location text
                organization = pf.stringify(cells[0].content[0]).strip()
                location = pf.stringify(cells[0].content[1]).strip()
                
                # Create a paragraph with organization and location spans
                combined_para = create_combined_para(organization, location)

                sub_divs = []
                for subcell in cells[1:]:
                    title = pf.stringify(subcell.content[0]).strip()
                    timeframe = pf.stringify(subcell.content[1]).strip()
                    title_span = pf.Span(pf.Str(title), classes=['resume-title'])
                    timeframe_span = pf.Span(pf.Str(timeframe), classes=['resume-timeframe'])
                    
                    # Add title and timeframe spans to a list, separated by space for proper formatting
                    sub_divs.append(pf.Para(title_span, pf.Space(), timeframe_span))

                # Create a div for the entry and include the combined organization and location paragraph
                entry_div = pf.Div(combined_para, *sub_divs, classes=['resume-header-entry'])
                divs.append(entry_div)

        return divs

def main(doc=None):
    return pf.run_filter(action, doc=doc)

if __name__ == '__main__':
    main()

