#!/usr/bin/env python3

import panflute as pf

def action(elem, doc):
    if isinstance(elem, pf.Table):
        content = pf.stringify(elem)
        if 'Email :' in content and 'Mobile :' in content:
            return []  # Return an empty list to remove this element

        def wrap_in_para(text, class_name):
            # This creates a paragraph with a span inside containing the text
            # The span allows us to use classes within a paragraph
            return pf.Para(pf.Span(pf.Str(text), classes=[class_name]))

        divs = []
        for row in elem.content:
            if len(row.content) >= 2:
                cells = row.content

                # Extract organization and location as text
                organization = pf.stringify(cells[0].content[0]).strip()
                location = pf.stringify(cells[0].content[1]).strip()
                
                # Wrap them in paragraphs with appropriate classes
                organization_para = wrap_in_para(organization, 'resume-organization')
                location_para = wrap_in_para(location, 'resume-location')

                sub_divs = []
                for subcell in cells[1:]:
                    title = pf.stringify(subcell.content[0]).strip()
                    timeframe = pf.stringify(subcell.content[1]).strip()
                    
                    # Wrap title and timeframe in paragraphs as well
                    title_para = wrap_in_para(title, 'resume-title')
                    timeframe_para = wrap_in_para(timeframe, 'resume-timeframe')
                    
                    # Add these paragraphs to a list for the current entry
                    sub_divs.extend([title_para, timeframe_para])

                # Create a div for the entry and include organization and location paragraphs
                entry_div = pf.Div(*[organization_para, location_para] + sub_divs, classes=['resume-header-entry'])
                divs.append(entry_div)

        return divs

def main(doc=None):
    return pf.run_filter(action, doc=doc)

if __name__ == '__main__':
    main()

