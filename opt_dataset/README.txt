## Steps for parsign data.
1. CVS data was obtained from {http://www.regulations.gov/#!docketBrowser;rpp=25;po=0;D=ICEB-2015-0002}
2. The following columns were deleted because they contained the same data
	- Document Type 			: data_for_all{PUBLIC SUBMISSIONS}
	- Attachment Count 			: data_for_all{N/A}
	- Submitter Last Name		: data_for_all{N/A}
	- Submitter First Name		: data_for_all{N/A}
	- Organization				: data_for_all{N/A}
	- Comment Start Date		: data_for_all{10/19/2015}
	- Comment Due Date			: data_for_all{11/18/2015}
	- Implementation Date		: data_for_all{N/A}
	- Effective Date			: data_for_all{N/A}
	- Related RINs				: data_for_all{N/A}
	- Document SubType			: data_for_all{N/A}
	- Subject					: data_for_all{N/A}
	- Abstract					: data_for_all{N/A}
	- Status					: data_for_all{Posted}
	- Source Citation			: data_for_all{N/A}
	- OMB Approval Number		: data_for_all{N/A}
	- FR Citation				: data_for_all{N/A}
	- Federal Register Number	: data_for_all{N/A}
	- Start End Page			: data_for_all{N/A}
	- Special Instructions		: data_for_all{N/A}
	- Legacy ID					: data_for_all{N/A}
	- Post Mark Date			: data_for_all{N/A}
	- File Type					: data_for_all{N/A}
	- Number Of Pages			: data_for_all{N/A}
	- Paper Width				: data_for_all{N/A}
	- Paper Length				: data_for_all{N/A}
	- Exhibit Type				: data_for_all{N/A}
	- Exhibit Location			: data_for_all{N/A}
	- Document Field_1			: data_for_all{N/A}
	- Document Field_2			: data_for_all{N/A}



3. The following columns are the ones used. 
	- Document Title / {userName}
	- Document ID / {documentID}
	- Posted Date / {postedDate}
	- Recieved Date / {receivedDate}
	- Document Detail / {comment}

4. Title lines were also deleted. 

5. Replace "Comment Submitted by " to "" --> $sed -i 's/Comment Submitted by //g' file.csv

6. Install NodeJS
7. Using Node's package manager install phantomjs: npm -g install phantomjs
8. Install selenium: pip install -U selenium
9. run python script: parse_csv.pu
10. Delete lines containing "N/A" --> $sed --in-place '/N\/A/d' opt.json






